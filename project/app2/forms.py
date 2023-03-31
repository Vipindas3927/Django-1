from django import forms
from .models import *

class user_data_form(forms.ModelForm):
    class Meta:
        model = user_data_model
        fields = '__all__'
