from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello</h1>")


def welcome(request):
    return HttpResponse("<h3>Welcome to Django</h3>")


def temp(request):
    return render(request, "temp.html")


def value(request):
    name = 'Vipindas'
    return render(request, "value.html", {'data': name})


def mulvalue(request):
    Name1 = 'Vipindas'
    Place1 = 'Kasaragod'
    return render(request, "value.html", {'name': Name1, 'place': Place1})


def minmax(request):
    l = [5, 9, 9, 6, 7, 3]
    min_nbr = l[0]
    max_nbr = l[0]
    for i in l:
        if i < min_nbr:
            min_nbr = i
        if i > max_nbr:
            max_nbr = i
    return render(request, "minmax.html", {'list': l, 'min_no': min_nbr, 'max_no': max_nbr})


def ageCat(request):
    a = []
    b = []
    l = [{'name': 'Anu', 'age': 19},
         {'name': 'Rahul', 'age': 14},
         {'name': 'Dhyan', 'age': 22},
         {'name': 'Amal', 'age': 20},
         {'name': 'Sumi', 'age': 23}]

    for i in l:
        if i['age'] < 20:
            a.append(i)
        else:
            b.append(i)
    j = 1
    for i in l:
        i['index'] = j
        j += 1

    j = 1
    for i in a:
        i['index'] = j
        j += 1

    j = 1
    for i in b:
        i['index'] = j
        j += 1

    return render(request, "ageCat.html", {'all': l, 'ls': a, 'gt': b})


def staticcss(request):
    return render(request, "staticfilecss.html")


def staticjs(request):
    return render(request, "staticfilejs.html")


def staticimg(request):
    return render(request, "staticfileimg.html")


def first(request):
    return render(request, "first.html")


def second(request):
    return render(request, "second.html")


def navigation(request):
    return render(request, "navigation.html")


def login(request):
    return render(request, "login.html")


def nav2(request):
    context = {"title": "HOME PAGE"}
    return render(request, "nav2.html", context)


def home2(request):
    context = {"title": "HOME"}
    return render(request, "home2.html", context)


def login2(request):
    context = {"title": "LOGIN"}
    return render(request, "login2.html", context)


def contact2(request):
    context = {"title": "CONTACT"}
    return render(request, "contact2.html", context)


def about2(request):
    context = {"title": "ABOUT"}
    return render(request, "about2.html", context)


# models

def studentDisplay(request):
    a = student.objects.all()
    return render(request, "studentDisplay.html", {'a': a})


def studentRegForm(request):
    return render(request, 'studentReg.html')


def studentReg(request):
    n = request.POST["name"]
    a = request.POST["age"]
    data = student(name=n, age=a)
    data.save()
    return HttpResponse("Data Stored")


def task(request):
    a = student.objects.all()
    l = []
    for i in a:
        n = i.name
        if n[0] == 'a' or n[0] == 'A':
            l.append(i)
    return render(request, "task.html", {'li': l, 'all': a})


def form1(request):
    return render(request, 'form1.html')


def Regform1(request):
    n = request.POST["name"]
    e = request.POST["email"]
    g = request.POST["gender"]
    c = request.POST["phone"]
    p = request.POST["pwd"]
    data = employee(name=n, email=e, gender=g, contact=c, password=p)
    data.save()
    return HttpResponse("Hello " + n + ",<br>" + "&nbsp;&nbsp;&nbsp;Data Stored Successfully...")


def loginForm(request):
    a = employee.objects.all()
    return render(request, 'loginForm.html', {'all': a})


def loginPage(request):
    a = employee.objects.all()
    e = request.POST["email"]
    key = 0
    for i in a:
        if e == i.email:
            key = 1
            e1 = i.email
            p1 = i.password
            n = i.name
            return HttpResponse("Hello " + n + ",<br>" + "&nbsp;&nbsp;&nbsp;Login Successfully...")
            break
    if key == 0:
        return HttpResponse(
            "<script>alert('Wrong user name or password')</script><div style='width:500px; height=500px;'><a href='loginForm'>go back</a></div>")


# form

# Registration data to model method 2
def studentForm2(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successful")
    return render(request, "StudentForm.html", {'form': form})


def employeeForm2(request):
    form = employeeForm()
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successful")
    return render(request, "employeeForm2.html", {'form': form})


def employeeLogin2(request):
    form = employeeLoginForm()
    if request.method == 'POST':
        form = employeeLoginForm(request.POST)
        a = employee.objects.all()
        e = request.POST["email"]
        p = request.POST["password"]
        key = 0
        for i in a:
            if e == i.email and i.password == p:
                key = 1
                n = i.name
                return HttpResponse("Hello " + n + ",<br>" + "&nbsp;&nbsp;&nbsp;Login Successfully...")
                break
        if key == 0:
            return HttpResponse(
                "<script>alert('Wrong user name or password')</script><div style='width:500px; height=500px;'><a href='employeeLogin2'>go back</a></div>")
    return render(request, "employeeForm2.html", {'form': form})


# model 3
def studentForm3(request):
    if request.method == "POST":
        form = studentForm31(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            a = form.cleaned_data["age"]
            data = student(name=n, age=a)
            data.save()
            return HttpResponse("Hello " + n + ",<br>" + "&nbsp;&nbsp;&nbsp;Data Stored Successfully...")
        else:
            return HttpResponse("Error")
    return render(request, "studentForm3.html")


def employeeForm3(request):
    if request.method == "POST":
        form = em3(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            e = form.cleaned_data["email"]
            g = form.cleaned_data["gender"]
            c = form.cleaned_data["contact"]
            p = form.cleaned_data["password"]
            data = employee(name=n, email=e, gender=g, contact=c, password=p)
            data.save()
            return HttpResponse("Hello " + n + ",<br>" + "&nbsp;&nbsp;&nbsp;Data Stored Successfully...")
        else:
            return HttpResponse("Error")
    return render(request, "employeeForm3.html")

def employeeLoginForm3(request):
    if request.method == "POST":
        form = emLogin3(request.POST)
        if form.is_valid():
            e = form.cleaned_data["email"]
            p = form.cleaned_data["password"]
            ListAll = employee.objects.all()
            key = 0
            for i in ListAll:
                if i.email == e and i.password == p:
                    key = 1
                    return HttpResponse("Hello " + i.name + ",<br>" + "&nbsp;&nbsp;&nbsp; Successfully Login...")
                    break
            if key == 0:
                return HttpResponse("Wrong username/password...<br><br><a href='employeeForm3'>click here to register</a>")
        else:
            return HttpResponse("Error")
    return render(request, "employeeLogin3.html")


#file uploading
def fileUploading(request):
    if request.method == 'POST':
        form = fileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            n = form.cleaned_data['name']
            f = form.cleaned_data['file']
            data = fileUpload(name=n, file=f)
            data.save()
            return HttpResponse("File uploaded successfully...")
        else:
            return HttpResponse("Error")
    return render(request, "fileUploadingForm.html")

def fileDisplay(request):
    images = fileUpload.objects.all()
    return render(request, "fileDisplay.html", {'i': images})

#food

def itemUpload(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.cleaned_data['iname']
            b = form.cleaned_data['iprice']
            c = form.cleaned_data['file']
            data = uploadModel(iname=a, iprice=b, file=c)
            data.save()
            return HttpResponse("<h3>Successfully Uploaded...</h3>")
        else:
            return HttpResponse("<h3>Submission Failed...</h3>")
    else:
        return render(request, "Fupload.html")
def itemDisplay(request):
    all = uploadModel.objects.all()
    name, price, files = [], [], []
    for i in all:
        path = i.file.url
        name.append(i.iname)
        price.append(i.iprice)
        files.append(path)
    return render(request, "Fitemdisplay.html", {'iname': name, 'iprice': price, 'file': files})
def itemOrder(request, name):
    all = uploadModel.objects.filter(iname=name)
    return render(request, "Fitemorder.html", {'data': all})
def itemBill(request):
    if request.method == 'POST':
        a = request.POST.get('iname')
        b = request.POST.get('iprice')
        c = request.POST.get('qty')
        if c == '':
            return HttpResponse("Item Quantity Must have some value")
        t = int(b) * int(c)
        data = itemBillModel(iname=a, iprice=b, qty=c, total=t)
        data.save()
    else:
        return HttpResponse("Error")
    return render(request, "Fitembill.html", {'iname': a, 'total': t, 'qty':c})

#login
def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user':current_user}
        return render(request, 'user_base_page.html', param)
    else:
        return redirect('signin')
    return render(request, 'user_login_page.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('psw')
        if User.objects.filter(username=uname).count() > 0:
            return HttpResponse('User name already exist.')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('home')
    else:
        return render(request, 'user_signup_page.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('psw')
        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse("Please enter valid user name and password.")
    return render(request, 'user_login_page.html')

def signout(request):
    try:
        del request.session['user']
    except:
        return redirect('signin')
    return redirect('signin')

#forign key

def userregister(request):
    return render(request, 'register.html')
def ureg(request):
    try:
        uid = request.POST['uid']
        name = request.POST['name']
        address = request.POST['address']
        un = request.POST['un']
        psd = request.POST['psd']
        date = User_Register(uid=uid, name=name, address=address, username=un, password=psd)
        date.save()
        return HttpResponse("Hi "+name+",<br>Successfully registered...")
    except:
        return HttpResponse("somthing went wrong...")
def testregister(request):
    return render(request, 'testreg.html')
def treg(request):
    try:
        tid = request.POST['tid']
        tname = request.POST['tname']
        tdes = request.POST['tdes']
        price = request.POST['price']

        data = Test_Register(tid=tid, tname=tname, tdescription=tdes, price=price)
        data.save()
        return HttpResponse("Hi ,<br>Successfully registered...")
    except:
        return HttpResponse("Somthing went wrong...")

def book(request):
    return render(request, 'book.html')
def booking(request):
    try:
        uid = request.POST['uid']
        tname = request.POST['tname']
        dt = request.POST['dt']
        data = Test_Book(uid=User_Register.objects.get(uid=uid), tname=Test_Register.objects.get(tname=tname),dt=dt)
        data.save()
        return HttpResponse("Hi,<br>Successfully registered...")
    except:
        return HttpResponse("somthing went wrong...")
def bookdetails(request):
    a = Test_Book.objects.all()
    return render(request, 'bookingdetails.html', {'data': a})
