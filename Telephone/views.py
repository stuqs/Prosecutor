from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return render(request, 'main1.html')