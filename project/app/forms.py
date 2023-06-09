from django import forms
from .models import *

#Mrthond 2
class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(render_value=True),
            'gender': forms.RadioSelect()
        }
class employeeLoginForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

#method 3
class studentForm31(forms.Form):
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()

class em3(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    gender = forms.CharField(max_length=15)
    contact = forms.IntegerField()
    password = forms.CharField(max_length=20)

class emLogin3(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class fileUploadForm(forms.Form):
    name = forms.CharField(max_length=20)
    file = forms.FileField()


#food
class uploadForm(forms.Form):
    iname = forms.CharField(max_length=20)
    iprice = forms.IntegerField()
    file = forms.FileField()
class itemBillForm(forms.Form):
    iname = forms.CharField(max_length=20)
    iprice = forms.IntegerField()
    qty = forms.IntegerField()
