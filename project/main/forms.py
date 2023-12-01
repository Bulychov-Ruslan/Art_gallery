from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

INPUT_CLASSES = 'form-control'
LABEL = 'labels'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control form-control-lg'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control form-control-lg'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control form-control-lg'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'form-control form-control-lg'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control form-control-lg'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'form-control form-control-lg'
    }))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'label': LABEL,
                'class': INPUT_CLASSES
            }),
            'first_name': forms.TextInput(attrs={
                'label': LABEL,
                'class': INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'label': LABEL,
                'class': INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'label': LABEL,
                'class': INPUT_CLASSES
            }),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'imageUser': forms.FileInput(attrs={
                'label': LABEL,
                'class': INPUT_CLASSES
            }),
            'bio': forms.Textarea(attrs={
                'label': LABEL,
                'class': INPUT_CLASSES
            }),
            'location': forms.TextInput(attrs={
                'label': LABEL,
                'class': INPUT_CLASSES
            }),
            'birth_date': forms.DateInput(attrs={
                'label': LABEL,
                'class': INPUT_CLASSES
            }),
        }


class MyForm(forms.Form):
    my_choices = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['my_choices'].choices = [(k, v) for k, v in my_dict.items()]

