from django.http.response import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url="/login/")
def index(request):
    return render(request, 'contactus/contactus.html')

def submit(request):
    return HttpResponse("Successful Msg Displayed....")