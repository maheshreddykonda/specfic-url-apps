from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def msd(request):
    return HttpResponse('msd is a great captain')


def msd1(request):
    return render(request,'app1.html')
