from django import forms
from .models import Names

class NameForm(forms.ModelForm) :
    class Meta :
        model = Names
        fields = ["name"]
