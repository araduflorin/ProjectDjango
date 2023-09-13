from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from aplicatie1.models import Location


# Create your views here.
class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['city' , 'country']
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['city', 'country']
    # fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')


class LocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'