from django.shortcuts import render
from Telephone.models import *
from Prosecutor.settings import FILTER


def positin_sort(emp_list):
    return sorted(emp_list, key=lambda x=emp_list: (-x.position.weight, x.surname))


def adder(where, what, key):
    if what in where:
        pass
    else:
        where[what] = key


def show_structure(employees, po_list):
    employees_dict = {}
    for pros_office in po_list:
        employees_dict[pros_office] = {'employees': [], 'departments': {}, 'division': {}}
    for employee in employees:
        if employee.prosecutors_office and employee.department and employee.division:
            adder(employees_dict[employee.prosecutors_office]['departments'], employee.department, {})
            adder(employees_dict[employee.prosecutors_office]['departments'][employee.department], employee.division, [])
            employees_dict[employee.prosecutors_office]['departments'][employee.department][employee.division].append(employee)
        elif employee.prosecutors_office and employee.department:
            adder(employees_dict[employee.prosecutors_office]['departments'], employee.department, {})
            adder(employees_dict[employee.prosecutors_office]['departments'][employee.department], 'employees', [])
            employees_dict[employee.prosecutors_office]['departments'][employee.department]['employees'].append(employee)
        elif employee.prosecutors_office and employee.division:
            adder(employees_dict[employee.prosecutors_office]['division'], employee.division, [])
            employees_dict[employee.prosecutors_office]['division'][employee.division].append(employee)
        elif employee.prosecutors_office:
            employees_dict[employee.prosecutors_office]['employees'].append(employee)
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

    print(show_structure(employee_list, po_list))

    return render(request, 'main.html', {'employees': positin_sort(employee_list), 'filter_header': 'filter_header.html',
                                         'table_header': 'table_header.html', 'table_loop': 'table_loop.html'})


def main_test(request):
    employee_list = Employee.objects.all()
    for k, v in request.GET.items():
        if FILTER.get(k) and v:
            field_query = {FILTER[k]: v}
            employee_list = employee_list.filter(**field_query)




    po_list = ProsecutorsOffice.objects.all()



    employees_dict = (show_structure(employee_list, po_list))



    return render(request, 'main2.html', {'employees_dict': employees_dict, 'filter_header': 'filter_header.html',
                                          'table_header': 'table_header.html', 'table_loop': 'table_loop.html'})

