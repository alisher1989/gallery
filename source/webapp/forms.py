from django import forms
from webapp.models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image', 'signature','like_amount', 'author']