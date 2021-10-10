from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url="/login/")
def index(request):
    return render(request, 'contactus/contactus.html')


# def mail(name, email, message):
#     send_mail(name,message, settings.EMAIL_HOST_USER,['adnan1470369258@gmail.com'],)

def submitting(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        category = request.POST.get('category')
        human = request.POST.get('human', 'off')
        message = request.POST.get('message')

        if name == "" or email == "":
            return render(request, 'contactus/error.html')

        else:
            subject = f'N.Msg Category: {category} & Human Verification Is:{human}'
            message = f'Name: {name}, Email: {email} & Message: {message}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["adnan1470369258@gmail.com"]
            send_mail(subject, message, email_from, recipient_list)
            return render(request, 'contactus/success.html')

    elif request.method!="POST":
        return render(request, 'contactus/error.html')

    else:
        return render(request, 'contactus/error.html')




def submit(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        opt1 = request.POST.get('opt-1', 'off')
        opt2 = request.POST.get('opt-2', 'off')
        opt3 = request.POST.get('opt-3', 'off')
        opt4 = request.POST.get('opt-4', 'off')
        opt5 = request.POST.get('opt-5', 'off')
        opt6 = request.POST.get('opt-6', 'off')

        if name == "" or email == "":
            return render(request, 'contactus/error.html')

        else:
            subject = f'N.Msg Category: {opt1,opt2,opt3,opt4,opt5,opt6}'
            message = f'Name: {name}, Email: {email}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["adnan1470369258@gmail.com"]
            send_mail(subject, message, email_from, recipient_list)
            return render(request, 'contactus/success.html')

    elif request.method!="POST":
        return render(request, 'contactus/error.html')

    else:
        return render(request, 'contactus/error.html')



def sending(request):
    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        subject1 = request.POST.get('subject1')
        message = request.POST.get('message')

        subject = f'New Msg, From: {fname}-{lname}'
        message = f'Email: {email}, Subject: {subject1} & Message: {message}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["adnan1470369258@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'contactus/success.html')

    elif request.method!="POST":
        return render(request, 'contactus/error.html')

    else:
        return render(request, 'contactus/error.html')




def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject1 = request.POST.get('subject1')
        message = request.POST.get('message')

        subject = f'New Msg, From: {name}'
        message = f'Email: {email}, Subject: {subject1} & Message: {message}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["adnan1470369258@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'contactus/success.html')

    elif request.method!="POST":
        return render(request, 'contactus/error.html')

    else:
        return render(request, 'contactus/error.html')