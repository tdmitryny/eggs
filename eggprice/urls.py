from django.urls import path
from . import views
from .views import ChartView

urlpatterns = [
    path('livechart/', ChartView.as_view(), name='chart'),
]