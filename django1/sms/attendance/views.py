from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import attendance
def attendance_list(request):
    attendance_records = attendance.objects.all()
    return HttpResponse(attendance_records)