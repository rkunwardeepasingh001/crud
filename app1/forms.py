from .models import Data
from django import forms
class Data_forms(forms.ModelForm):
  class Meta:
    model=Data
    fields='__all__'
    