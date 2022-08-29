from django.db import models

# Create your models here.


'''
This model is used to display the data on the box in the details page
'''
from directoryPage.models import course

class level2(models.Model):
    courseKey = models.ForeignKey(course, on_delete=models.CASCADE)
    Project_name= models.CharField(max_length=200)
    total_topics = models.IntegerField()
    # status= models.BooleanField(default=False) #optionla yet to decide
    result=[
        ('Mastery', 'Mastery'),
        ('Exmplary', 'Exmplary'),
        ('Satisfactory', 'satisfactory')
    ]
    result = models.CharField(max_length=100, choices=result)

    def __str__(self):
        return self.Project_name


# class level3(models.Model):
#     level3Key = models.ForeignKey(level2, on_delete=models.DO_NOTHING)
#     Task_name= models.CharField(max_length=300)
