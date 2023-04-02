from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'app3Temp/home.html')
def admin_home(request):
    return render(request, 'app3Temp/admin_home.html')
def student_home(request):
    return render(request, 'app3Temp/student_home.html')
def teacher_home(request):
    return render(request, 'app3Temp/teacher_home.html')

def student_signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_student = True
            f.save()
            return home(request)
    return render(request, 'app3Temp/student_signup.html', {'form': form})
def teacher_signup(request):
    form1 = CustomUserCreationForm()
    form2 = TeacherRegistrationForm()
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        teacher_form = TeacherRegistrationForm(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save(commit=False)
            user.is_teacher = True
            user.save()
            tr = teacher_form.save(commit=False)
            tr.user =user
            tr.save()
            print(request, 'You have successfully registered as Teacher')
            return home(request)
        else:
            print(request,'Error... Form Invalid...')
    return render(request, 'app3Temp/teacher_signup.html', {'form1': form1, 'form2': form2})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_superuser == True:
            login(request, user)
            return admin_home(request)
        elif user and user.is_student:
            login(request, user)
            return student_home(request)
        elif user and user.is_teacher:
            login(request, user)
            return teacher_home(request)
        else:
            return HttpResponse("Invalid user credential...")
    return render(request, 'app3Temp/login.html')
def user_logout(request):
    logout(request)
    return home(request)








