from django.contrib import admin
from .models import Post, Like, Comment
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


# class CustomUserAdmin(UserAdmin):
#     fieldsets =(
#         (None, {'fields': ('date_of_birth', 'height',)}),
#     ) + UserAdmin.fieldsets
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('date_of_birth', 'height',)}),
#     )
#     list_display = UserAdmin.list_display + ('date_of_birth', 'height', )


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class LikeAdminForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'content',  'photo', 'user')
    fields = ('content', 'title',  'photo', 'user')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "Фото не установлено"
    get_photo.short_description = 'Миниатюра'


class LikeAdmin(admin.ModelAdmin):
    form = LikeAdminForm
    list_display = ('id', 'user', 'post', 'comment', 'created_at')
    fields = ('id', 'user', 'post', 'comment', 'created_at')


class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields ='__all__'


class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ('id', 'content', 'created_at')
    fields = ('id', 'content', 'created_at')


#admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(MyUser)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment)

admin.site.site_title = 'Управление постами'
admin.site.site_header = 'Управление постами'
