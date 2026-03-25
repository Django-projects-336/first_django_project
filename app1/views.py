from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
# url --> 127.0.0.1:8000/app1/page1
def page1(request) :
        return HttpResponse("<h1> Hello Page 1 </h1>")
