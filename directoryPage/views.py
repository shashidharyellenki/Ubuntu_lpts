from traceback import print_tb
from urllib.request import HTTPRedirectHandler
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

# from .models import StudentCard, course, Add_Course

from django.contrib import messages

# from newUserReg.models import Register
from django.core.paginator import Paginator
from django.core.mail import send_mail

# Importing all models from the models.py file

from .models import Student,Course,Units,Units_content,Enrollments

def index(request):
    studentDetails = Student.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            studentDetails = studentDetails.filter(Name__iexact=keyword)
    # used for searching by courseName
    if 'selectspec' in request.GET:
        spec = request.GET['selectspec']
        if spec == 'FirstYear':
            studentDetails = studentDetails.filter(acadamicYear__iexact=spec)
        elif spec == 'ALL':
            studentDetails = Student.objects.all()
        elif spec == 'SecondYear':
            studentDetails = studentDetails.filter(acadamicYear__iexact=spec)
        elif spec == 'Passed_out':
            studentDetails = studentDetails.filter(acadamicYear__iexact=spec)
        else:
            studentDetails = studentDetails.filter(specalization__iexact=spec)
    context = {
        'student': studentDetails
    }
    return render(request, 'pages/index.html', context)



def student(request, student_id):
    # storing all the data in the variable
    data = Course.objects.all()


    #outCome - SubjectNames that student Enrolled during his course type: Queryset
    filter_data = data.filter(Course_Student_Relation=student_id).values() 
    # Outcome- This CourseList will store all the objects of the courses that student enrolled during his/her academics
    
    # outcome - will displayes the profile of the student
    profile = Student.objects.all().filter(id=student_id)

    # grades = Enrollments.objects.all().filter(StudentKey_id=student_id).values()


    # Paginator Function
    item_paginator = Paginator(filter_data, 8)
    page_number = request.GET.get('page')
    filter_data = item_paginator.get_page(page_number)
    if 'keywordd' in request.GET:
        spc = request.GET['keywordd']
        if spc:
            filter_data = data.filter(Name__iexact=spc)

    if 'spc' in request.GET:
        spc = request.GET['spc']
        if spc == 'SoftSkills':
            filter_data = data.filter(Tags__iexact=spc)

        elif spc == "continousCredits-ss":
            filter_data = data.filter(Tags__iexact=spc)
        elif spc == "continousCredits-ps":
            filter_data = data.filter(Tags__iexact=spc)
        elif spc == "continousCredits-hk":
            filter_data = data.filter(Tags__iexact=spc)
        elif spc == 'Technical':
            filter_data = data.filter(Tags__iexact=spc) 
    context = {
        'studentData': filter_data, 
        'profile': profile,
    }

    return render(request, 'pages/studentdetails.html', context)

'''
This piece of code is used for sending mails to the students
'''
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

'''
This piece of code is used for displaying the courses and progress.
'''

def details(request, Units_id):
    units = Units.objects.all().filter( Course_Unit_Relation=Units_id).values()
   
    context={
      'data_set':units,
    }
        
    return render(request,'pages/level2.html', context)

def CourseIndepthDetails(request,moredetails_id):
    UC = Units_content.objects.all().filter(Units_UC_Relation=moredetails_id)
    context={
        "dataSet":UC
    }
    return render(request, 'pages/moreDetails.html', context)

# for updating the status
def update_status(request):
    UC = Units_content.objects.all()
    if 'status' in request.GET:
        response = request.GET['status']
        response = response.split(',')
        print(response)
        if response[0] == 'completed':
            res = UC.get(id=response[1])
            res.Grades=response[0]
            res.save()
            sendmail("I have succfully completed the ", res.Name, 'requesting for viva session')


        if response[0] == 'Incomplete':
            res = UC.get(id=response[1])
            res.Grades=response[0]
            res.save()
        
        if response[0]=='Doubt':
            res = UC.get(id=response[1])
            res.Grades=response[0]
            res.save()
            sendmail("I have doubt in",res.Name ,'Requesting for Doubt clearing sesseion!')            
            
    return render(request, 'pages/moreDetails.html')



# sending mail heliping function
def sendmail(text,content, subject):
    send_mail(
                f'{subject}',
                f'Hello sir/madam {text} {content}',
                'yellenkishashidhar@gmail.com',
                ['yellenkishashidhar@msitprogram.net'],
                
            )
