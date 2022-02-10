from django.db import models
from my_blog import settings
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)


class Like(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT)
