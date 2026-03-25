from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
# url --> 127.0.0.1:8000/app2/page2
def page2(request) :
        return HttpResponse("<h1> Hello Page 2 </h1>")

def page3(request) :
        return HttpResponse("<h1> Hello Page 3 </h1>")