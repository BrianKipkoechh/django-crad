from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import student


def home(request):
    data=student.objects.all()
    return render(request, 'index.html', {'data':data})
def insertData(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        query=student(name=name,email=email,age=age,gender=gender)

        query.save()
        return redirect('/')
    else:
        return render(request,'index.html')
def updateData(request,id):
     if request.method == 'POST':
         name = request.POST.get("name")
         email = request.POST.get("email")
         age = request.POST.get("age")
         gender = request.POST.get("gender")

         rekebisha=student.objects.get(id=id)
         rekebisha.name=name
         rekebisha.email=email
         rekebisha.age=age
         rekebisha.gender=gender
         rekebisha.save()
         return redirect('/')
     else:
        d = student.objects.get(id=id)
        return render(request,'edit.html',{'d':d})
def delete(request,id):
    d=student.objects.get(id=id)
    d.delete()
    return redrect('/')
