from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django.contrib.auth.password_validation import *


class LoginForm(AuthenticationForm):
    error_messages = {
        'required': 'Email yoki parol kiriting.',
        'invalid_login': 'Email yoki parol noto\'g\'ri.',
        'unique': 'Mavjud',
    }
    username = forms.EmailField(
        label = 'Email kiriting',
        widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email kiriting'}),
    )
    password= forms.CharField(
        label = 'Parol',
        widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Parol'}),
    )
class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Parollar bir-biriga mos emas.",
    }
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')


    first_name = forms.CharField(
        label = 'Ism',
        widget = forms.TextInput(attrs={'class':'form-control'}),
    )

    last_name = forms.CharField(
        label = 'Familiya',
        widget = forms.TextInput(attrs={'class':'form-control'}),
    )

    email = forms.EmailField(
        label = 'Email kiriting',
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email kiriting'}),
    )
    phone = forms.CharField(
        label = 'Telefon raqam',
        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'raqam'}),
    )

    password1 = forms.CharField(
        label = 'Parol',
        widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Parol'}),
    )
    password2 = forms.CharField(
        label = 'Parolni tasdiqlash',
        widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Parolni takrorlang'}),
    )


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'phone')

    first_name = forms.CharField(
        label = 'Ism',
        widget = forms.TextInput(attrs={'class':'form-control'}),
    )
    last_name = forms.CharField(
        label = 'Familiya',
        widget = forms.TextInput(attrs={'class':'form-control'}),

    )
    email = forms.EmailField(
        label = 'Email kiriting',
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email kiriting'}),
    )
    phone = forms.CharField(
        label = 'Telefon raqam',
        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'raqam'}),
    )
