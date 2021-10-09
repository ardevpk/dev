from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'p2/p2.html')


def about(request):
    return render(request, 'p2/about.html')