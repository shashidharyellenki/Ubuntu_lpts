from django.db import models
# Create your models here.
'''
#old models

class StudentCard(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    Email = models.EmailField(max_length=100, blank=False)
    bio= models.TextField(max_length=400)
    Years=[
        ('FirstYear','FirstYear'),
        ('SecondYear','SecondYear'),
        ('Alumni','Alumni'),
    ]
    acadamicYear= models.CharField(max_length=20, choices=Years)
    spcs=[
        ('Full Stack Webdevelopment', 'Full Stack Webdevelopment'),
        ('Machine Learning', 'Machine Learning'),
        ('Artifical Intelligence', 'Artifical Intelligence'),
        ('Data Science', 'Data Science'),
        ('Ethical Hacking', 'Ethical Hacking'),
        ('Cloud Computing', 'Cloud Computing'),
    ]
    specalization=models.CharField(max_length=50, choices=spcs)
    RollNumber = models.IntegerField(blank=False)
    Image = models.ImageField(blank=False)

    def __str__(self):
        return self.Name

class course(models.Model):
    studentKey = models.ForeignKey(StudentCard, on_delete=models.DO_NOTHING)
    courseName = models.CharField(max_length=50, blank=False)
    marks = models.IntegerField()
    remarks = models.TextField(max_length=200)
    statusChoicee = [
        ('Complete','Complete'),
        ('Incomplete', 'Incomplete')
    ]
    status = models.CharField(max_length=50, choices=statusChoicee, blank=False)
    courseEnrolledDate = models.DateField(auto_now_add=True)
    courseDuration = models.IntegerField()
    courseTypeChoice=[
        ('SoftSkills', 'SoftSkills'),
        ('continousCredits-ss', 'continousCredits-ss'),
        ('continousCredits-ps', 'continousCredits-ps'),
        ('continousCredits-hk', 'continousCredits-hk'),
        ('Technical', 'Technical'),

    ]
    continousCredits = models.CharField(max_length=50, choices=courseTypeChoice)

    def __str__(self):
        return self.courseName



# to add courses to the students
class Add_Course(models.Model):
    Student_name = models.ForeignKey(StudentCard, on_delete=models.CASCADE)
    Course_to_be_Add = models.ForeignKey(course, on_delete=models.CASCADE)


    def __str__(self):
        return self.Student_name.Name

'''

# Student table
class Student(models.Model):
    Name= models.CharField(max_length=100)
    Email= models.EmailField()
    Phone=models.IntegerField()
    Years=[
        ('FirstYear','FirstYear'),
        ('SecondYear','SecondYear'),
        ('Alumni','Alumni'),
    ]
    acadamicYear= models.CharField(max_length=20, choices=Years)
    spcs=[
        ('Full Stack Webdevelopment', 'Full Stack Webdevelopment'),
        ('Machine Learning', 'Machine Learning'),
        ('Artifical Intelligence', 'Artifical Intelligence'),
        ('Data Science', 'Data Science'),
        ('Ethical Hacking', 'Ethical Hacking'),
        ('Cloud Computing', 'Cloud Computing'),
    ]
    specalization=models.CharField(max_length=50, choices=spcs)
    RollNumber = models.CharField(max_length=20,blank=False)
    Image = models.ImageField(blank=False)

    def __str__(self):
        return self.Name+ " "+ self.Email

'''
This table is used to store only Course details
'''
class Course(models.Model):
    Course_Student_Relation = models.ManyToManyField(Student, through="Enrollments")
    Name= models.CharField(max_length=100)
    Max_marks=models.IntegerField()
    Max_duration=models.IntegerField()
    credits=models.IntegerField()
    TagsList=[
        ('Technical', 'Technical'),
        ('SoftSkills', 'SoftSkills'),
        ('Presentations', 'Presentations'),
        ('Group Discussions', 'Group Discussions'),
        ('Problems Solving', 'Problem Solving'),
        ('Hacker Rank', 'Hacker Rank')
    ]
    Tags = models.CharField(max_length=20, choices=TagsList, null=True, blank=True)
    Grades_Options=[
        ('Enrolled',"Enrolled"),
        ('Mastery','Mastery'),
        ('Exemplary','Exemplary'),
        ('Incomplete','Incomplete'),
        ('Pending','Pending')
    ]
    Grades = models.CharField(max_length=100, choices=Grades_Options, null=True)
    Remarks = models.TextField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.Name

'''
This table is used to add Units to the courses
week1day1
'''
class Units(models.Model):
    Course_Unit_Relation = models.ManyToManyField(Course)
    Name= models.CharField(max_length=200)
    Created_At= models.DateTimeField(auto_now_add=True)
    Grades_Options=[
        ('Enrolled',"Enrolled"),
        ('Mastery','Mastery'),
        ('Exemplary','Exemplary'),
        ('Incomplete','Incomplete'),
        ('Pending','Pending')
    ]
    Grades = models.CharField(max_length=100, choices=Grades_Options, null=True)
    Remarks = models.TextField(max_length=500, blank=True, null=True)
    dlevel=[
        ('Easy','Easy'),('Medium', 'Medium'), ('Advanced', 'Advanced')
    ]
    Difficulty = models.CharField(max_length=10, choices=dlevel)

    def __str__(self):
        return self.Name

'''
This table is used to content to thhe Units table
'''

class Units_content(models.Model):
    Units_UC_Relation = models.ForeignKey(Units, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Created_At=models.DateField(auto_now_add=True)
    Image = models.ImageField(upload_to='media', blank=True)
    Text_box = models.TextField(max_length=1000)
    Grades_Options=[
        ('complete',"complete"),
        ('Doubt','Doubt'),
        ('Incomplete','Incomplete'),
    ]
    Grades = models.CharField(max_length=100, choices=Grades_Options, null=True)
    Remarks = models.TextField(max_length=500, blank=True, null=True)
    dlevel=[
        ('Easy','Easy'),('Medium', 'Medium'), ('Advanced', 'Advanced')
    ]
    Difficulty = models.CharField(max_length=10, choices=dlevel)

    def __str__(self):
        return self.Name

'''
Using this table Instructor can enroll student into the courses. After completing the course any Instruuctor
can evaluate the student's performance and add result.
'''

class Enrollments(models.Model):
    StudentKey = models.ForeignKey(Student, on_delete=models.CASCADE)
    CourseKey = models.ForeignKey(Course, on_delete=models.CASCADE)
    Course_Enrolled_Date = models.DateField(auto_now_add=True)
    # 
   

    def __str__(self):
        return self.StudentKey.Name
