from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='blog'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
]