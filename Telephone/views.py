from django.shortcuts import render
from django.http import HttpResponseRedirect
from Telephone.models import *
from Prosecutor.settings import FILTER


def positin_sort(emp_list):
    return sorted(emp_list, key=lambda x=emp_list: (-x.position.weight, x.surname))


def main_page(request):
    prosecutorsoffices = ProsecutorsOffice.objects.all()
    return render(request, 'main.html', {'prosecutorsoffices': prosecutorsoffices, 'table_header': 'table_header.html',
                                         'table_loop': 'table_loop.html'})


def main_with_filter(request):
    employee_list = Employee.objects.all()
    for k, v in request.GET.items():
        if FILTER.get(k) and v:
            field_query = {FILTER[k]: v}
            employee_list = employee_list.filter(**field_query)




    PO = ProsecutorsOffice.objects.all()












    return render(request, 'main.html', {'employees': positin_sort(employee_list), 'filter_header': 'filter_header.html',
                                         'table_header': 'table_header.html', 'table_loop': 'table_loop.html'})

