from crispy_forms.helper import FormHelper
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms.models import inlineformset_factory
from django.views.generic import CreateView, ListView
from schemas.models import Schema, Column


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
        column_formset = inlineformset_factory(
            Schema, Column, fields=('name', 'column_types', 'order'),
            labels={'name': 'Column name', 'column_types': 'Type', 'order': 'Order'},
            can_order=False, can_delete=False
        )
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





