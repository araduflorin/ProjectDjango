from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from aplicatie2.forms import CompaniesClass
from aplicatie2.models import Companies


# Create your views here.
class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    form_class = CompaniesClass
    template_name = "aplicatie1/location_form.html"

    def get_success_url(self):
        return reverse('aplicatie2:lista_companii')

class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    form_class = CompaniesClass
    template_name = "aplicatie2/company_index.html"

class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    form_class = CompaniesClass
    template_name = "aplicatie1/location_form.html"

    def get_success_url(self):
        return reverse('aplicatie2:lista_companii')

