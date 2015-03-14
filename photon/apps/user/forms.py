from django import forms
from .models import User
from django.utils.translation import ugettext_lazy as _


class Form_Settings_User(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar',
                  'website', 'facebook', 'twitter', 'googleplus', 'instagram']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Nombre De Usuario'}),
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
                'id': 'profile_input'}),
        }
        error_messages = {
            "avatar": {
                "required": "Seleccione una imagen.",
            },
            "username": {
                "unique": "El nombre de usuario ya esta ocupado.",
            },
        }

    def save(self, commit=True):
        instance = super(Form_Settings_User, self).save(commit=False)
        instance.username = self.cleaned_data['username'].replace(" ", "")
        if commit:
            instance.save()
        return instance
