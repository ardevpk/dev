from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url="/login/")
def index(request):
    return render(request, 'p4/p4.html')

# def ptdetails(request):
#     return render(request, 'two/portfolio-details.html')