from django.urls import path
from .views import *

urlpatterns =[
    path('', Main.as_view(), name='main'),
    path('home', ViewPost.as_view(), name='home')
]