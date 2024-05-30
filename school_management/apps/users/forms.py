from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Role

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'two_factor_enabled', 'sso_id')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'two_factor_enabled', 'sso_id')

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']
