from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class RegistrationForm(UserCreationForm):
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
