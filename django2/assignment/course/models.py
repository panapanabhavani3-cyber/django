from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=50)
    course_fee = models.IntegerField()
    trainer_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=20)
    start_date = models.DateField()
    number_of_seats = models.IntegerField()
    course_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name