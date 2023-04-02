from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

# Display/Read
def user_display(request):
    userdata =user_data_model.objects.all()
    return render(request, "app2Temp/display.html", {'userdata': userdata})
# Insert/Create
def insert_user(request):
    form = user_data_form()
    if request.method == 'POST':
        form = user_data_form(request.POST)
        if form.is_valid():
            form.save()
            return user_display(request)
    return render(request, 'app2Temp/insert.html', {'form': form})
# Remove/Delete
def delete_user(request, id):
    a = user_data_model.objects.get(pk=id)
    a.delete()
    return user_display(request)
# Edit/Update
def update_user(request, id):
    uid = user_data_model.objects.get(pk=id)
    form = user_data_form(instance=uid)
    if request.method == 'POST':
        uid = user_data_model.objects.get(pk=id)
        form = user_data_form(request.POST, instance=uid)
        if form.is_valid():
            form.save()
            return  user_display(request)
    return render(request, 'app2Temp/update.html', {'form': form})

