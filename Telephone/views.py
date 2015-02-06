from django.shortcuts import render
from django.http import HttpResponse
from Telephone.models import *

def main_page(request):


    prosecutorsoffices = ProsecutorsOffice.objects.order_by('name')



    # for emp in employees:
    #     #Сделать проверку на безопастность (наличие только чисел с - и ;)
    #      emp.work_telephone = "<br>".join(emp.work_telephone.split(';'))
    #      emp.private_telephone = "<br>".join(emp.private_telephone.split(';'))

    return render(request, 'main.html', {'prosecutorsoffices': prosecutorsoffices, 'table_header': 'table_header.html',
                                         'table_loop': 'table_loop.html'})

