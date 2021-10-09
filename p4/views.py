from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'p4/p4.html')