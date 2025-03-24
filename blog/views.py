from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 3

class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'  # This tells the view to look for 'slug' in the URL
    slug_field = 'slug'  # This tells the view which field to use for the slug lookup
