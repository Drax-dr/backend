from django.shortcuts import render
from .models import Student, Lecturer, Parents


class UserProfileView:
    model = Student

class LecturerProfileView:
    model = Lecturer

class AdminProfileView:
    pass

class LoginView:
    pass
