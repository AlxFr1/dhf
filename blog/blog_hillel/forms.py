from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture')


class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=400, help_text="Describe your problem in a box", widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

