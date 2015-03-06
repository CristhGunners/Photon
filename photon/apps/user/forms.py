from django import forms
from .models import User


class Form_Settings_User(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar',
                  'website', 'facebook', 'twitter', 'googleplus', 'instagram']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Nombre De Usuario'}),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Apellido'}),
            'website': forms.TextInput(attrs={
                'placeholder': 'Sitio Web'}),
            'facebook': forms.TextInput(attrs={
                'placeholder': 'Facebook'}),
            'twitter': forms.TextInput(attrs={
                'placeholder': 'Twitter'}),
            'googleplus': forms.TextInput(attrs={
                'placeholder': 'Google+'}),
            'instagram': forms.TextInput(attrs={
                'placeholder': 'Instagram'}),
            'avatar': forms.FileInput(attrs={
                'class': 'upload', 'id': 'files'}),
        }
