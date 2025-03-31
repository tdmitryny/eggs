from django.shortcuts import render
from django.views.generic import DetailView
from .models import About


class AboutView(DetailView):
    model = About
    template_name = 'about/about.html'
    context_object_name = 'about'

# Create your views here.
    def get_object(self):
        return About.objects.first() 
