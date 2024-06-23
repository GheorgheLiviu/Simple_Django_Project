from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput
import random


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})


class UserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['last_name', 'first_name',
                  # 'username',
                  'password1','password2', 'email']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs.update({
        #     'class': 'form-control', 'placeholder': 'Type a username'
        # })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Type your password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Retype your password'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Enter your last name'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': "Enter your first name"
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Enter your email address'
        })
