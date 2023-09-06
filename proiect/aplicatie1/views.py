from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from aplicatie1.models import Location


# Create your views here.
class CreateLocationView(CreateView):
    model = Location
    fields = ['city' , 'country']
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('/')

class LocationView(ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'