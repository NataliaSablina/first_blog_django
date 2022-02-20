from django import forms
from .models import MyUser, Post, Category, Comment
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={"class": "form-control"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo', 'category')
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.TextInput(attrs={"class": "form-control"}),
            'photo': forms.FileInput(attrs={"class": "form-control", "required": "true"}),
            'category': forms.Select(attrs={"class": "form-control"})
        }


class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class RegistrationForm(UserCreationForm):
    captcha = CaptchaField()
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={"class": "form-control"}))
    second_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={"class": "form-control"}))
    age = forms.IntegerField(label='Возраст', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if password1 != password2:
    #         raise forms.ValidationError('Passwords do not match.')
    #     user = User.objects.get(pk=self.user_id)
    #     password_histories = PasswordHistory.objects.filter(
    #         user=user
    #     )
    #     for pw in password_histories:
    #         if check_password(password2, pw.password):
    #             raise forms.ValidationError('That password has already been used')
    #     return password2

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'second_name', 'age', 'password1', 'password2')
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "second_name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
