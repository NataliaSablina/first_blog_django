from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class Main(ListView):
    template_name = 'blog/main_page.html'

    def get_queryset(self):
       pass


class ViewPost(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


