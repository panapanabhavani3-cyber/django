from django.db import models

class Attendance(models.Model):
    student_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name