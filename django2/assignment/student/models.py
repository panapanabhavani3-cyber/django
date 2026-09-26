from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    date_of_admission = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.student_name
