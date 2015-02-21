from django.shortcuts import render
from Telephone.models import *
from Prosecutor.settings import FILTER


def positin_sort(emp_list):
    """
    :param emp_list: list of employees
    :return: sorted by position.weight list
    """
    return sorted(emp_list, key=lambda x=emp_list: (-x.position.weight, x.surname))


def adder(where, what, value):
    """
    Check if the dictionary has key(what), if not add to this key value(value)
    :param where: dictionary that checks
    :param what: key of dictionary
    :param value: value, that may be added
    :return: None
    """
    if what in where:
        pass
    else:
        where[what] = value


def show_structure(employees):
    """
    Create structure (dict) from eployees list
    :param employees: list of employees
    :return:
    """
    employees_dict = {}
    for employee in positin_sort(employees):
        adder(employees_dict, employee.prosecutors_office, {'employees': [], 'departments': {}, 'divisions': {}})
        if employee.prosecutors_office and employee.department and employee.division:
            adder(employees_dict[employee.prosecutors_office]['departments'], employee.department, {})
            adder(employees_dict[employee.prosecutors_office]['departments'][employee.department], 'divisions', {})
            adder(employees_dict[employee.prosecutors_office]['departments'][employee.department]['divisions'], employee.division, [])
            employees_dict[employee.prosecutors_office]['departments'][employee.department]['divisions'][employee.division].append(employee)
        elif employee.prosecutors_office and employee.department:
            adder(employees_dict[employee.prosecutors_office]['departments'], employee.department, {})
            adder(employees_dict[employee.prosecutors_office]['departments'][employee.department], 'employees', [])
            employees_dict[employee.prosecutors_office]['departments'][employee.department]['employees'].append(employee)
        elif employee.prosecutors_office and employee.division:
            adder(employees_dict[employee.prosecutors_office]['divisions'], employee.division, [])
            employees_dict[employee.prosecutors_office]['divisions'][employee.division].append(employee)
        elif employee.prosecutors_office:
            employees_dict[employee.prosecutors_office]['employees'].append(employee)
    return employees_dict


def main_with_filter(request):
    """
    Main page with filter
    """
    employee_list = Employee.objects.all()
    for k, v in request.GET.items():
        if FILTER.get(k) and v:
            field_query = {FILTER[k]: v}
            employee_list = employee_list.filter(**field_query)
    employees_dict = show_structure(employee_list)
    return render(request, 'main.html', {'employees_dict': employees_dict, 'filter_header': 'filter_header.html',
                                         'table_header': 'table_header.html', 'table_loop': 'table_loop.html'})

