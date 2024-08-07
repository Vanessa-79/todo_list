from django import forms
from .models import *


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
        }
