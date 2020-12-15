from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from schemas.models import Schema


class SchemaListView(ListView):
    model = Schema


class SchemaCreateView(LoginRequiredMixin, CreateView):
    model = Schema
    fields = ['name', 'column_separator', 'string_separator']
    success_url = reverse_lazy('SchemaListView')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




