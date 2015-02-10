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
    emp = ''
    print(request.GET)


    emp_name = request.GET.get('emp_name', default=None)
    telephone = request.GET.get('telephone', default=None)
    if emp_name or telephone:
        emp = Employee.objects.filter(surname__icontains=emp_name, work_telephone__icontains=telephone)
    elif request.GET.get('division', default=None):

        if request.GET.get('department', default=None):

            if request.GET.get('pros_office', default=None):
                pass

            # just department
            pass
            # just division
        pass
    else:
        # all view
        pass


    return render(request, 'main1.html', {'emp': emp})






def view_for_test(request, *args, **kwargs):

    print(request.GET)
    # return HttpResponseRedirect('/')
    prosecutorsoffices = ProsecutorsOffice.objects.all()
    return render(request, 'main1.html', {'prosecutorsoffices': prosecutorsoffices})