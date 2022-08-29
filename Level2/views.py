from django.shortcuts import render

# Importing all the courses from the courses model
from directoryPage.models import course, Add_Course

# importing models from the level2
from .models import level2
# Create your views here.
def details(request, projects_id):
    # tempdata = Add_Course.objects.filter(Course_to_be_Add_id=projects_id)
    # temp = tempdata.filter()
    # print(tempdata)

    # temp = level2.objects.filter(courseKey=projects_id)
    # print(temp)


    
    
    filterData = level2.objects.all().filter(courseKey_id=projects_id)
    context={
        'data_set':filterData
    }
    return render(request,'pages/level2.html',context)

