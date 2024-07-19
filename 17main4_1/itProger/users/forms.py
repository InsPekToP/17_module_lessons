from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(forms.Form):
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label ='Введите Email',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Введите Email'})
        )
    username = forms.CharField(
        label ='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /,_',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Введите логин'})
        )
    password1 = forms.CharField(
        label ='Введите пароль',
        required=True,
        help_text='Пароль не должен быть маленьким и простым',
        #отображение в виде точек(для пароля)
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Введите пароль'})
        )
    password2 = forms.CharField(
        label ='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Подтвердите пароль'})
        )

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label ='Введите Email',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Введите Email'})
        )
    username = forms.CharField(
        label ='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /,_',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Введите логин'})
        )
    class Meta:
        model = User
        fields = ['username','email']

class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label ='Загрузить фото',
        required=False,
        #удалить кнопку очистить
        widget=forms.FileInput
        )
    
    class Meta:
        model = Profile
        fields = ['img'] 
