from django.urls import path
from .views import *

urlpatterns =[
    path('', Main.as_view(), name='main'),
    path('home', ViewPosts.as_view(), name='home'),
    path('like_post/<int:post_id>', like_post, name='like_post'),
    path('like_comment/<int:comment_id>', like_comment, name='like_comment'),
    path('user/<int:user_id>', UserDetailView.as_view(), name='get_user'),
    path('signup', UserRegisterView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('post/<int:post_id>', PostView.as_view(), name='get_post'),
    path('create_post', CreatePost.as_view(), name='create_post'),
    path('logout', user_logout_view, name='logout'),
    path('create_category', CreateCategory.as_view(), name='create_category'),
    path('create_comment/<int:post_id>', CreateComment.as_view(), name='create_comment'),
    path('comments_view/<int:post_id>', comments_view, name='comments_view'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]