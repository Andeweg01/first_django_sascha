from django import forms
from .models import Item


class ItemForm(forms.Modelform):
    class Meta:
        model = Item
        fields = ['name', 'done']