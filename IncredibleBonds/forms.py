from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'email', 'is_patient', 'is_doctor', 'is_parent', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = UserChangeForm.Meta.fields
