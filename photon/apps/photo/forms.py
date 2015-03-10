from django import forms
from .models import Photo


class Form_Photo(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image', 'tags']
        labels = {
            'image': (''),
        }
        help_texts = {
            'tags': ('Tags separados por una ","'),
        }
        widgets = {
            'image': forms.FileInput(
                attrs={'class': 'upload', 'id': 'background_input'}),
        }
        error_messages = {
            "image": {
                "required": "Seleccione un Imagen",
            },
            "tags": {
                "required": "Ingrese al menos un Tag",
            }
        }
