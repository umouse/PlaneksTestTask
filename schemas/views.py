from crispy_forms.helper import FormHelper
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms.models import inlineformset_factory
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView
from django.views.generic.edit import FormMixin
from schemas.tasks import generate_data_task

from schemas.models import Schema, Column, DataSet
from schemas.forms import DataSetForm

column_formset = inlineformset_factory(
            Schema, Column, fields=('name', 'column_types', 'order'),
            labels={'name': 'Column name', 'column_types': 'Type', 'order': 'Order'},
            can_order=False, can_delete=False
        )


class SchemaListView(ListView):
    model = Schema


class ColumnFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = 'bootstrap/table_inline_formset.html'


class SchemaCreateView(LoginRequiredMixin, CreateView):
    model = Schema
    fields = ['name', 'column_separator', 'string_character']
    success_url = reverse_lazy('SchemaListView')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        helper = ColumnFormSetHelper()
        data["helper"] = helper
        if self.request.POST:
            data["columns"] = column_formset(self.request.POST)
        else:
            data["columns"] = column_formset()
        return data

    def form_valid(self, form):
        form.instance.user = self.request.user
        context = self.get_context_data()
        columns = context["columns"]
        self.object = form.save()
        if columns.is_valid():
            columns.instance = self.object
            columns.save()
        return super().form_valid(form)


class SchemaUpdateView(LoginRequiredMixin, UpdateView):
    model = Schema
    fields = ['name', 'column_separator', 'string_character']
    success_url = reverse_lazy('SchemaListView')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        helper = ColumnFormSetHelper()
        data["helper"] = helper
        if self.request.POST:
            data["columns"] = column_formset(self.request.POST, instance=self.object)
        else:
            data["columns"] = column_formset(instance=self.object)
        return data

    def form_valid(self, form):
        form.instance.user = self.request.user
        context = self.get_context_data()
        columns = context["columns"]
        self.object = form.save()
        if columns.is_valid():
            columns.instance = self.object
            columns.save()
        return super().form_valid(form)


class SchemaDeleteView(DeleteView):
    model = Schema
    success_url = reverse_lazy('SchemaListView')


class DataSetView(FormMixin, ListView):
    model = DataSet
    form_class = DataSetForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(schema_id=self.schema_id)


    def form_valid(self, form):
        form.instance.schema_id = self.schema_id
        form.instance.status = DataSet.Status.PROCESSING

        dataset = form.save()

        generate_data_task.delay(dataset.id)

        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        self.schema_id = kwargs["pk"]
        generate_data_task.delay(2)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.path
