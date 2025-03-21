from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
