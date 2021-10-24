from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return render(request, 'main/main.html')

def pages(request):
    return HttpResponse("<br> <br> <br><center><h1>Page Not Found</h1></center>")