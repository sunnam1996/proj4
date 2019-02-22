from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def registerinput(request):
    return render(request,'register.html')
def logininput(request):
    return render(request,'login.html')
def regester(request):
    return render(request,'login.html')
def register(request):
    a=request.POST["userid"]
    b = request.POST["passid"]
    c = request.POST["username"]
    d = request.POST["address"]
    e = request.POST["country"]
    f = request.POST["zip"]
    g = request.POST["email"]
    h = request.POST["sex"]
    i = request.POST["en"]
    j = request.POST["nonen"]
    k = request.POST["desc"]
    print(a,b,c,d,e,f,g,h,i,j,k)
    return HttpResponse("registration success")
def login(request):
    a = request.POST["un"]
    b = request.POST["pwd"]
    print(a,b)
    return HttpResponse("login success")
# Create your views here.
