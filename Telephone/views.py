from django.shortcuts import render
from django.http import HttpResponseRedirect
from Telephone.models import *

def main_page(request):
    print(request.GET)
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
    if request.GET['emp_name'] or request.GET['telephone']:
        pass
    elif request.GET['division']:
        if request.GET['department']:

            if request.GET['pros_office']:
                pass

            # just department
            pass
            # just division
        pass
    else:
        # all view
        pass





def view_for_test(request, *args, **kwargs):

    print(request.GET)
    # return HttpResponseRedirect('/')
    prosecutorsoffices = ProsecutorsOffice.objects.all()
    return render(request, 'main1.html', {'prosecutorsoffices': prosecutorsoffices})