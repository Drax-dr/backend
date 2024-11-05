from django.db import models
from assignments.models import Assignments

class Student(models.Model):
    name        =  models.CharField(max_length=30, name="Name",default="")
    studentID   =  models.CharField(max_,length=10, name="ID",default="", unique=True,error_messages={'unique': "A user with that ID already exists.",})
    phoneNumber =  models.CharField(max_length=10, name="Phone number",default="",unique=True)
    fatherNummber = models.CharField(max_length=10, name="Parent/Guardian number",default="")
    profilePic  =  models.ImageField(name="Photo",default="",upload_to="assets/images")
    grade = models.IntegerField(default=8)
    assignmentsCompleted = models.ManyToManyField(Assignments)
    

class Lecturer(models.Model):
    name        =  models.CharField(max_length=30, name="Name",default="")
    id   =  models.CharField(max_length=10, name="mID",default="")
    phoneNumber =  models.CharField(max_length=10, name="Phone number",default="")
    profilePic  =  models.ImageField(name="Photo",default="")
    videoUploaded = models

class Parents(models.Model):
    pass
