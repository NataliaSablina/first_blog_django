from django.db import models
from my_blog import settings
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="my_posts")

    def get_like_number(self):
        return self.like_set.all().count()

    def is_liked(self, user):
        print(self.like_set.filter(user=user))
        return True

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)


class Like(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="Пользователь")
    post = models.ForeignKey(Post, on_delete=models.PROTECT, verbose_name="Пост", blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT, verbose_name="Комментарий", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата лайка', blank=True, null=True)
