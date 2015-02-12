from django.shortcuts import render
from django.http import HttpResponseRedirect
from Telephone.models import *


FILTER = {
    'employee': 'surname__icontains',
    'telephone': 'work_telephone__icontains',
    'division': 'division__name__icontains',
    'department': 'department__name__icontains',
    'prosecutors_office': 'prosecutors_office__name__icontains',
    }

def main_page(request):
    prosecutorsoffices = ProsecutorsOffice.objects.all()
    return render(request, 'main.html', {'prosecutorsoffices': prosecutorsoffices, 'table_header': 'table_header.html',
                                         'table_loop': 'table_loop.html'})


def main_with_filter(request):
    employee_list = Employee.objects.all()
    filtered = False
    for k, v in request.GET.items():
        if FILTER.get(k) and v:
            filtered = True
            field_query = {FILTER[k]: v}
            employee_list = employee_list.filter(**field_query)
    if filtered:
        return render(request, 'main1.html', {'employees': employee_list})
    else:
        # Return all view
        return render(request, 'main1.html', {'employees': ''})

