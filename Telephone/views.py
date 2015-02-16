from django.shortcuts import render
from django.http import HttpResponseRedirect
from Telephone.models import *
from Prosecutor.settings import FILTER


def positin_sort(emp_list):
    return sorted(emp_list, key=lambda x=emp_list: (-x.position.weight, x.surname))

def show_structure(employees, po_list):
    employees_dict = {}
    for pros_office in po_list:
        employees_dict[pros_office] = {'employees': [], 'departments': {'employees': [], 'division': []}, 'division': []}
    for employee in employees:
        if employee.prosecutors_office and employee.department and employee.division:
            employees_dict[employee.prosecutors_office]
            employees_dict[employee.prosecutors_office]['departments']['division'].append(employee.division)
            # print(employees_dict[employee.prosecutors_office][employee.department][employee.division])#.add(employee)



    return employees_dict

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




    po_list = ProsecutorsOffice.objects.all()
    #
    # department_list = Department.objects.all()
    # divisions_list = Division.objects.all()
    # employees_dict = {}
    #


    print(show_structure(employee_list, po_list))
    print(employee_list)


    # Division-department
    # Division-prosecutors_office
    #
    # Department-prosecutors_office

    return render(request, 'main.html', {'employees': positin_sort(employee_list), 'filter_header': 'filter_header.html',
                                         'table_header': 'table_header.html', 'table_loop': 'table_loop.html'})
