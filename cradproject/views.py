from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
    return redirect('/')
def handlesignup(request):
    if request.method == ('POST'):
        username=request.POST.get("username")
        password=request.POST.get("password")

        myuser=User.objects.create_user(username,password)
        myuser.save()
    return render(request,'sign up.html')
def handlelogin(request):
    if request.method == ('POST'):
        username = request.POST.get("username")
        password = request.POST.get("password")

        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request,'login.html')
def handlelogout(request):
        logout(request)
        return redirect('/signup')


