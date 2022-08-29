from urllib.request import HTTPRedirectHandler
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .models import StudentCard, course, Add_Course

from django.contrib import messages

# from newUserReg.models import Register
from django.core.paginator import Paginator
from django.core.mail import send_mail


# Create your views here.
def index(request):
    student = StudentCard.objects.all()  # stroing all the data from the database into student varibale
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            student = student.filter(Name__iexact=keyword)
    # used for searching by courseName
    if 'selectspec' in request.GET:
        spec = request.GET['selectspec']
        if spec == 'FirstYear':
            student = student.filter(acadamicYear__iexact=spec)
        elif spec == 'ALL':
            student = StudentCard.objects.all()
        elif spec == 'SecondYear':
            student = student.filter(acadamicYear__iexact=spec)
        elif spec == 'Passed_out':
            student = student.filter(acadamicYear__iexact=spec)
        else:
            student = student.filter(specalization__iexact=spec)
    context = {
        'student': student
    }
    return render(request, 'pages/index.html', context)


def student(request, student_id):
    # storing all the data in the variable
    data = course.objects.all() 
    test = Add_Course.objects.all()
    filter_data = data.filter(studentKey_id=student_id) #data
    profile = StudentCard.objects.all().filter(id=student_id)

    # Paginator Function
    item_paginator = Paginator(filter_data, 8)
    page_number = request.GET.get('page')
    filter_data = item_paginator.get_page(page_number)
    if 'keywordd' in request.GET:
        spc = request.GET['keywordd']
        if spc:
            filter_data = data.filter(courseName__iexact=spc)

    if 'spc' in request.GET:
        spc = request.GET['spc']
        if spc == 'SoftSkills':
            filter_data = data.filter(continousCredits__iexact=spc)

        elif spc == "continousCredits-ss":
            filter_data = data.filter(continousCredits__iexact=spc)
        elif spc == "continousCredits-ps":
            filter_data = data.filter(continousCredits__iexact=spc)
        elif spc == "continousCredits-hk":
            filter_data = data.filter(continousCredits__iexact=spc)
        elif spc == 'Technical':
            filter_data = data.filter(continousCredits__iexact=spc)
    context = {
        'studentData': filter_data,
        'profile': profile,
    }

    return render(request, 'pages/studentdetails.html', context)


def send_email(request):
    if request.method == 'POST':
        email = request.POST['Email']
        send_mail(
            'Application form',
            'www.google.com',
            'yellenkishashidhar@gmail.com',
            [email, 'yellenkishashidhar@gmail.com'],
            fail_silently=False
        )
    return redirect('/')
