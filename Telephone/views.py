from django.shortcuts import render, redirect
from Telephone.models import *
from Prosecutor.settings import FILTER
from Telephone.tools import *
from django.http import HttpResponse


def main_with_filter(request):
    """
    Main page with filter
    """
    print(request)
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
    return render(request, 'structure.html', {'structure': structure})


def show_structure(request, po=None, department=None, division=None):
    employee_list = Employee.objects.all()
    if po:
        employee_list = employee_list.filter(prosecutors_office__name__icontains=po)
    if department:
        employee_list = employee_list.filter(department__name__icontains=department)
    if division:
        employee_list = employee_list.filter(division__name__icontains=division)
    if employee_list:
        employees_dict = create_employee_structure(employee_list)
        return render(request, 'main2.html', {'employees_dict': employees_dict, 'table_header': 'table_header.html',
                                              'table_loop': 'table_loop.html'})
    else:
        return redirect('/structure/')


def ajax_department(request):
    print(request)
    from django.core import serializers
    json_subcat = serializers.serialize("json", Department.objects.filter(prosecutors_office__id=request.GET.get('prosecutors_office_id')))
    return HttpResponse(json_subcat, content_type="application/javascript")


def ajax_division(request):
    print(request)
    from django.core import serializers
    json_subcat = serializers.serialize("json", Division.objects.filter(department__id=request.GET.get('department_id')))
    return HttpResponse(json_subcat, content_type="application/javascript")