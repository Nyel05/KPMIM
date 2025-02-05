from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.description}"

   

class Mentor(models.Model) :
    mentorCd = models.CharField(max_length=4 , primary_key=True)
    mentorName = models.TextField()
    mentorEmail = models.EmailField(default= 'default@gmail.com')

    def __str__(self):
        return f"{self.mentorName} ({self.mentorCd})"

class Student(models.Model):
    id = models.CharField(max_length=12, primary_key = True)
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 12)
    course_code = models.ForeignKey(Course, on_delete = models.CASCADE)
    Status = models.CharField(max_length=3, default='MP')
# Create your models here.
