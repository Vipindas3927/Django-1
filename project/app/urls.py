"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('welcome/', views.welcome, name='welcome'),
    path('temp/', views.temp, name='temp'),
    path('value/', views.value, name='value'),
    path('mulvalue/', views.mulvalue, name='mulvalue'),
    path('minmax/', views.minmax, name='minmax'),
    path('agecat/', views.ageCat, name='agecat'),
    path('staticcss/', views.staticcss, name='staticcss'),
    path('staticjs/', views.staticjs, name='staticjs'),
    path('staticimg/', views.staticimg, name='staticimg'),
    path('first/', views.first, name="first"),
    path('second/', views.second, name="second"),
    path('navigation/', views.navigation, name="navigation"),
    path('login/', views.login, name="login"),
    path('nav2/', views.nav2, name="nav2"),
    path('home2/', views.home2, name="home2"),
    path('login2/', views.login2, name="login2"),
    path('contact2/', views.contact2, name="contact2"),
    path('about2/', views.about2, name="about2"),
    path('students/', views.studentDisplay, name='studentDisplay'),
    path('studentRegForm/', views.studentRegForm, name='studentRegForm'),
    path('studentReg', views.studentReg, name='studentReg'),
    path('task', views.task, name='task'),
    path('form1/', views.form1, name='form1'),
    path('regForm1', views.Regform1, name='regForm1'),
    path('loginForm', views.loginForm, name='loginForm'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('studentForm2', views.studentForm2, name='studentForm2'),
    path('employeeForm2', views.employeeForm2, name='employeeForm2'),
    path('employeeLogin2', views.employeeLogin2, name='employeeLogin2'),
    path('studentForm3', views.studentForm3, name='studentForm3'),
    path('employeeForm3', views.employeeForm3, name='employeeForm3'),
]
