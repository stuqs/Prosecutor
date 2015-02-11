from django.shortcuts import render
from django.http import HttpResponseRedirect
from Telephone.models import *

def main_page(request):

    # print(request.GET['pros_office'])
    prosecutorsoffices = ProsecutorsOffice.objects.all()
    # if request.GET['pros_office']:
    #     prosecutorsoffices = ProsecutorsOffice.objects.filter(id=request.GET['pros_office'])
    #
    # def sort_employees(self):
    #     return sorted(self.employees.all(), key=(lambda x=self.employees.all(): x.position.weight), reverse=True)

    # name
    # telephone
    # pros_office



    return render(request, 'main.html', {'prosecutorsoffices': prosecutorsoffices, 'table_header': 'table_header.html',
                                         'table_loop': 'table_loop.html'})



def main_with_filter(request):
    employees = ''
    print(request.GET)


    emp_name = request.GET.get('employee')
    telephone = request.GET.get('telephone')
    division = request.GET.get('division')
    department = request.GET.get('department')
    prosecutors_office = request.GET.get('prosecutors_office')

    if emp_name or telephone:
        print(division)
        employees = Employee.objects.filter(surname__icontains=emp_name, work_telephone__icontains=telephone)
                                            # division__name__icontains=division, department__name__icontains=department)
    elif division:
        employees = Employee.objects.filter(division__icontains=division)
        # return render(request, 'main1.html', {'employees': employees})
        if department:

            if prosecutors_office:
                pass

            employees = Employee.objects.filter(division__icontains=division)
            pass
            # just division
        pass
    else:
        # all
        pass


    return render(request, 'main1.html', {'employees': employees})

