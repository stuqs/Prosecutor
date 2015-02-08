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



    return render(request, 'main2.html', {'prosecutorsoffices': prosecutorsoffices, 'table_header': 'table_header.html',
                                         'table_loop': 'table_loop.html'})


def view_for_test(request, *args, **kwargs):

    print(request.GET)
    # return HttpResponseRedirect('/')
    prosecutorsoffices = ProsecutorsOffice.objects.all()
    return render(request, 'main1.html', {'prosecutorsoffices': prosecutorsoffices})