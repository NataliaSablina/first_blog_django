from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View
from .models import Post, Like


class Main(TemplateView):
    template_name = 'blog/main_page.html'

    def get_queryset(self):
        pass


class ViewPost(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


def like_post(request, post_id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=post_id)
        user = request.user
        try:
            like = Like.objects.get(post=post, user=user)
            like.delete()
        except Like.DoesNotExist:
            like = Like.objects.create(post=post, user=user)

    return redirect('home')
