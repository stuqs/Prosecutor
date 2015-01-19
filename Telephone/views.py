from django.shortcuts import render
from django.http import HttpResponse
from Telephone.models import *

def main_page(request):
    employee = Employee.objects.order_by('name')
    for emp in employee:
         emp.work_telephone = "<br>".join(emp.work_telephone.split(';'))
         emp.private_telephone = "<br>".join(emp.private_telephone.split(';'))
    return render(request, 'main.html', {'employee':employee})