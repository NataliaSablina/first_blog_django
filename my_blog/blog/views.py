from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import *
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        context = {'form': form}
        return render(request, 'blog/login.html', context)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                **data
            )
            if user is not None:
                login(request, user)
        else:
            print(form.errors)
        return redirect('home')


class UserDetailView(View):
    def get(self, request, user_id):
        user = MyUser.objects.get(pk=user_id)
        return render(request, 'blog/user_page.html', {"user": user})


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


class UserRegisterView(View):
    def get(self, request):
        form = forms.RegistrationForm()
        context = {'form': form}
        return render(request, 'blog/signup.html', context)

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
        else:
            print(form.errors)
        return redirect('home')
