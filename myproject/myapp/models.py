from django.db import models

# Create your models here.

class Student(models.Model):

    s_name=models.CharField(max_length=200)
    s_phone=models.CharField(max_length=200)
    s_email=models.EmailField()
    s_marks=models.IntegerField()