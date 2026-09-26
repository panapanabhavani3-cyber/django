from django.db import models


class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    salary = models.IntegerField()
    joining_date = models.DateField()
    currently_working = models.BooleanField(default=True)

    def __str__(self):
        return self.employee_name
