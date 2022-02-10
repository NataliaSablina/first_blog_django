from django.contrib import admin
from .models import Post, Like, Comment
from django import forms
from django.utils.safestring import mark_safe


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'content',  'photo', 'user')
    fields = ('id', 'title', 'content',  'photo', 'user')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "Фото не установлено"
    get_photo.short_description = 'Миниатюра'


admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)

admin.site.site_title = 'Управление постами'
admin.site.site_header = 'Управление постами'
