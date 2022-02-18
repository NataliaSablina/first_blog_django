from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import *
from . import forms
from django.contrib import messages


def like_comment(request, comment_id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_id)
        user = request.user
        try:
            like = Like.objects.get(comment=comment, user=user)
            like.delete()
        except Like.DoesNotExist:
            like = Like.objects.create(comment=comment, user=user)

    return redirect('comments_view', comment.post.pk)


def comments_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = post.comment_set.all()
    return render(request, "blog/post_comments.html", {"comments": comments, "post": post})


class CreateComment(LoginRequiredMixin, View):
    def get(self, request, post_id):
        form = forms.CommentForm()
        context = {"form": form, }
        return render(request, "blog/add_comment.html", context)

    def post(self, request, post_id):
        form = forms.CommentForm(request.POST)
        post = Post.objects.get(pk=post_id)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('comments_view', post_id)
        return redirect('create_comment', post_id)


class CreateCategory(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.CategoryForm()
        context = {'form': form}
        return render(request, 'blog/addcategory.html', context)

    def post(self, request):
        form = forms.CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')


class CreatePost(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.PostForm()
        context = {'form': form}
        return render(request, 'blog/addpost.html', context)

    def post(self, request):
        form = forms.PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.photo = request.FILES.get('photo')
            post.user = request.user
            post.save()
            return redirect('get_post', post.pk)
        else:
            return redirect('create_post')


class PostView(View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        return render(request, 'blog/current_post.html', {"post": post})


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        context = {'form': form}
        return render(request, 'blog/login.html', context)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            form.cleaned_data = form.clean()
            data = form.cleaned_data
            user = authenticate(
                **data
            )
            if user is not None:
                login(request, user)
                return redirect('get_user', user.pk)

        else:
            print(form.errors)
        return redirect('login')


class UserDetailView(View):
    def get(self, request, user_id):
        user = MyUser.objects.get(pk=user_id)
        return render(request, 'blog/user_page.html', {"user": user})


class Main(TemplateView):
    template_name = 'blog/main_page.html'

    def get_queryset(self):
        pass


class ViewPosts(ListView):
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
            login(request, user)
            return redirect('get_user', user.pk)
        else:
            messages.error(request, 'Ошибка регистрации')
            print(form.errors)
        return redirect('signup')


def user_logout_view(request):
    logout(request)
    return redirect('home')
