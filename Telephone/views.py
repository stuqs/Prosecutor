from django.shortcuts import render
from Telephone.models import *
from Prosecutor.settings import FILTER
from Telephone.tools import *


def main_with_filter(request):
    """
    Main page with filter
    """
    employee_list = Employee.objects.all()
    for k, v in request.GET.items():
        if FILTER.get(k) and v:
            field_query = {FILTER[k]: v}
            employee_list = employee_list.filter(**field_query)
    employees_dict = create_employee_structure(employee_list)
    po_list = ProsecutorsOffice.objects.all()
    department_list = Department.objects.all()
    division_list = Division.objects.all()
    return render(request, 'main.html', {'employees_dict': employees_dict, 'filter_header': 'filter_header.html',
                                         'table_header': 'table_header.html', 'table_loop': 'table_loop.html',
                                         'po_list': po_list, 'department_list': department_list, 'division_list': division_list})


def tree_structure(request):
    structure = create_tree_structure(ProsecutorsOffice.objects.all())
    return render(request, 'structure1.html', {'structure': structure})


def test_f(request, po=None, department=None, division=None):
    if po:
        print(po)
    if department:
        print(department)
    if division:
        print(division)