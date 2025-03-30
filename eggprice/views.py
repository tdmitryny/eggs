from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ChartView(TemplateView):
    template_name = "charts/chart.html"

