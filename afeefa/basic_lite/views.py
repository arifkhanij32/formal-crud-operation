from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    return render(request,"home2.html")
def insert(request):
    data=Emp(S_NO=1,NAME='ARIFKHAN',AGE=32)
    data.save()
    
    return redirect("select")
def select(request):
    data=Emp.objects.all()
    return render(request,"home2.html",{"result":data})

