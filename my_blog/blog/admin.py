from django.contrib import admin
from .models import Post, Like, Comment
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MyUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'second_name', 'age', 'pic')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'first_name', 'second_name', 'age', 'pic', 'is_active', 'is_staff')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'second_name', 'age', 'pic', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'second_name', 'age', 'pic',)}),
        ('Permissions', {'fields': ('is_staff',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'second_name', 'age', 'pic', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


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
    list_display = ('id', 'title', 'content',  'photo', 'user', 'category')
    fields = ('content', 'title',  'photo', 'user', 'category')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "Фото не установлено"
    get_photo.short_description = 'Миниатюра'


class LikeAdmin(admin.ModelAdmin):
    form = LikeAdminForm
    list_display = ('id', 'user', 'post', 'comment', 'created_at')
    fields = ('user', 'post', 'comment')


class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields ='__all__'


class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ('id', 'user', 'post', 'content', 'created_at')
    fields = ('user', 'post', 'content')


admin.site.register(MyUser, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_title = 'Управление постами'
admin.site.site_header = 'Управление постами'
