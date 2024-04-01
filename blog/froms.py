from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your username',
            'class': 'shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Your password',
            'class': 'shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your username',
            'class': 'shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        }))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Your email',
            'class': 'shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        }))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Your password',
            'class': 'shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        }))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Your password',
            'class': 'shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        }))


class AddPost(forms.ModelForm):

    class Meta:
        INPUT_CLASS = "mt-3 shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
        model = Post
        fields = ('title', 'category', 'content', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            }),
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'cols': '30',
                'rows': '10',
            }),
        }


class EditPost(forms.ModelForm):

    class Meta:
        INPUT_CLASS = "mt-3 shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
        model = Post
        fields = ('title', 'category', 'content', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            }),
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'cols': '30',
                'rows': '10',
            }),
        }


class AddComment(forms.ModelForm):
    class Meta:
        INPUT_CLASS = "mt-3 shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
        model = Comment
        fields = ('message',)
        widgets = {
            'message': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'cols': '20',
                'rows': '2'
            })
        }
