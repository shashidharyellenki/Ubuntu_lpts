from django.shortcuts import redirect, render
from . models import Register
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
def indexx(request):
    if request.method=='POST':
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        Birthday_date = request.POST['Birthday_date']
        username = request.POST['Username']
        if password == password2:
            if Register.objects.filter(email=email).exists():
                return render(request, 'forms/errorMessage.html' )
            else:
                register = Register(FirstName= FirstName,LastName=LastName,email=email, phone=phone, password=password, password2=password2,Birthday_date=Birthday_date, username=username)
                register.save()
                return render(request, 'forms/successMessage.html' )
    else:

        return render(request, 'forms/registration.html')


def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']

        if Register.objects.filter(username=Username).exists():
            if Register.objects.filter(password=password).exists():
                context={
                    "username":Username
                }
                return render(request, 'forms/registration.html',context)
            else:
                return HttpResponse("Wrong password")
        else:
            return HttpResponse("Invalid username")
    else:
        return render(request,'forms/registration.html')

def success(request):
    return render(request, 'forms/successMessage.html')