from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from data_siswa_app.models import CustemUser

def admin_home(request):
    return render(request, "hod_template/home_content.html")

def add_staff(request):
    return render(request,'hod_template/add_staff_template.html')

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method not Found")
    else:
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        nama_depan=request.POST.get("nama_depan")
        nama_belakang=request.POST.get("nama_belakang")
        alamat=request.POST.get("alamat")
        try:
            user=CustemUser.objects.create_user(username=username,password=password,email=email,nama_belakang=nama_belakang,nama_depan=nama_depan,user_type=2)
            user.staffs.alamat=alamat
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("add_staff")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("add_staff")
    
    
