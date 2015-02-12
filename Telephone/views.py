from django.shortcuts import render
from django.http import HttpResponseRedirect
from Telephone.models import *
from Prosecutor.settings import FILTER


def positin_sort(self):
    return sorted(self.objects.all(), key=(lambda x=self.objects.all(): x.position.weight), reverse=True)

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
        return render(request, 'main.html', {'employees': employee_list, 'filter_header': 'filter_header.html', 'table_header': 'table_header.html',
                                         'table_loop': 'table_loop.html'})
    else:
        # Return Po vashemu zaprosu nichego ne naideno
        return render(request, 'main.html', {'employees': '', 'filter_header': 'filter_header.html', 'table_header': 'table_header.html',
                                         'table_loop': 'table_loop.html'})

