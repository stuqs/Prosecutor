from django.shortcuts import render, redirect
from Telephone.models import *
from Telephone.settings import FILTER
from Telephone.tools import *
from django.http import HttpResponse
from Prosecutor.settings import BASE_DIR

DB_CHANGE = True


def main_with_filter(request):
    """
    Main page with filter
    """
    po_list = ProsecutorsOffice.objects.all()
    department_list = Department.objects.all()
    division_list = Division.objects.all()
    if not request.GET:
        return render(request, 'main.html', {'employees_dict': {}, 'filter_header': 'filter_header.html',
                                             'table_header': 'table_header.html', 'table_loop': 'table_loop.html',
                                             'po_list': po_list, 'department_list': department_list, 'division_list': division_list,
                                             'table_attribute': 'table_attribute.html', 'filter': True})
    else:
        employee_list = Employee.objects.all()
        for k, v in request.GET.items():
            if FILTER.get(k) and v:
                if k == 'telephone':
                    v = v.replace(' ', '')
                    v = v.replace('-', '')
                field_query = {FILTER[k]: v}
                employee_list = employee_list.filter(**field_query)
        employees_dict = create_employee_structure(employee_list)
        return render(request, 'main.html', {'employees_dict': employees_dict, 'filter_header': 'filter_header.html',
                                             'table_header': 'table_header.html', 'table_loop': 'table_loop.html',
                                             'po_list': po_list, 'department_list': department_list, 'division_list': division_list,
                                             'table_attribute': 'table_attribute.html', 'filter': True})


def tree_structure(request):
    """
    Create tree structure from all PO
    """
    structure = create_tree_structure(ProsecutorsOffice.objects.all())
    return render(request, 'structure.html', {'structure': structure})


def show_structure(request, po=None, department=None, division=None):
    """
    If employees exist in input, then show, else back to structure
    :param po: Name of PO
    :param department: Name of department
    :param division: Name of division
    """
    employee_list = Employee.objects.all()
    if po:
        employee_list = employee_list.filter(prosecutors_office__id=po)
    if department:
        if employee_list.filter(department__id=department):
            employee_list = employee_list.filter(department__id=department)
        elif employee_list.filter(division__id=department):
            employee_list = employee_list.filter(division__id=department)
    if division:
        employee_list = employee_list.filter(division__id=division)
    if employee_list:
        employees_dict = create_employee_structure(employee_list)
        return render(request, 'main.html', {'employees_dict': employees_dict, 'table_header': 'table_header.html',
                                             'table_loop': 'table_loop.html', 'table_attribute': 'table_attribute.html',
                                             'filter': False})
    else:
        return redirect('/structure/')


def ajax_department(request):
    """
    Ajax request to db, for select in po return list of departments
    :return: json object
    """
    from django.core import serializers
    json_subcat = serializers.serialize("json", Department.objects.filter(prosecutors_office__id=request.GET.get('prosecutors_office_id')))
    return HttpResponse(json_subcat, content_type="application/javascript")


def ajax_division(request):
    """
    Ajax request to db, for select in departments return list of divisions
    :return: json object
    """
    from django.core import serializers
    json_subcat = serializers.serialize("json", Division.objects.filter(department__id=request.GET.get('department_id')))
    return HttpResponse(json_subcat, content_type="application/javascript")


def database_changed():
    global DB_CHANGE
    DB_CHANGE = True


def download_file(request):
    global DB_CHANGE
    path = os.path.abspath(BASE_DIR + '/media/files/Telephones.xlsx')
    if DB_CHANGE:
        if create_file(Employee.objects.all(), path):
            DB_CHANGE = False
        fsock = open_file(path)
        if not fsock:
            DB_CHANGE = True
            redirect('/404')
        else:
            response = HttpResponse(fsock, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="Telephones.xlsx"'
            return response
    else:
        fsock = open_file(path)
        if fsock:
            response = HttpResponse(fsock, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="Telephones.xlsx"'
            return response
        else:
            DB_CHANGE = True
            return redirect('/404')