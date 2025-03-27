#from django.http import HttpResponse
from django.shortcuts import render

def layout(request):
    #return HttpResponse("Hello World! I'm Home.")
    return render(request, 'layout.html')