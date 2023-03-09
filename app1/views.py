from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def pspk(request):
    return HttpResponse('<h1><marquee bgcolor="red">Power star pawan kalyan</marquee></h1>')
