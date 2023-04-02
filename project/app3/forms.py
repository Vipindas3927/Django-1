from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone')
class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = TeacherRegistration
        fields = ('Qualification', 'Introduction_brief')



