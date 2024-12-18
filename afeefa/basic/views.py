from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    if request.method=="POST":
        s=request.POST["s"]
        n=request.POST["Name"]
        a=request.POST["Age"]
        k=Emp(S_NO=s,NAME=n,AGE=a)
        k.save()  
        return redirect('show')
    return render(request,"home.html")

def show(request):
     all=Emp.objects.all()
     return render(request,"show.html",{'ans':all})
     
def update(request,u):
        k=Emp.objects.get(S_NO=u)
        if request.method=="POST":
            nu=request.POST["Name"]
            au=request.POST["Age"]
            k.NAME=nu
            k.AGE=au
            k.save()
            return redirect('show')
        else:

            return render(request,"update.html",{'an':k})

def delete(request,l):
     k=Emp.objects.get(S_NO=l)
     k.delete()
     return redirect('show')



          
     

