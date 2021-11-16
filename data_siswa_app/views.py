from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def showDemoPage(request):
    return render(request,"demo.html")

def showLoginPage(request):
    return render(request, "loginPage.html")

def dologin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        return HttpResponse("email : "+request.POST.get("email")+"Password : "+request.POST.get("password"))