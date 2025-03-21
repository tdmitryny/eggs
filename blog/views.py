from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 10
