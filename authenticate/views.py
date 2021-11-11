from django.http.response import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def login_view(request):
    msg = None
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            if User.objects.filter(username = username).first():
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    user.last_login
                    user.save()
                    if 'next' in request.POST:
                        return redirect(request.POST['next'])
                    else:
                        return redirect('/')
                else:
                    msg = "Incorrect Password"
                    messages.warning(request, "Incorrect Password")
                    if 'next' in request.POST:
                        return redirect(f"/login/?next={request.POST['next']}", {"msg" : msg})
                    else:
                        return render(request, 'authenticate/login.html', {"msg" : msg})
                    # return render(request, 'authenticate/login.html', {"msg" : msg})
            else:
                msg = "Username Doesn't Exists"
                messages.error(request, "Username Doesn't Exists")
                if 'next' in request.POST:
                    return redirect(f"/login/?next={request.POST['next']}", {"msg" : msg})
                else:
                    return render(request, 'authenticate/login.html', {"msg" : msg})
            
        elif request.method!='POST':
            msg = "Please Enter Your Credentials"
            messages.success(request, "Please Enter Your Credentials")
            if 'next' in request.POST:
                return redirect(f"/login/?next={request.POST['next']}", {"msg" : msg})
            else:
                return render(request, 'authenticate/login.html', {"msg" : msg})

    except Exception as e:
        msg = f"Error Please Try Again..... Error: {e}..."
        messages.error(request, f"Error Please Try Again..... Error: {e}...")
        if 'next' in request.POST:
            return redirect(f"/login/?next={request.POST['next']}", {"msg" : msg})
        else:
            return render(request, 'authenticate/login.html', {"msg" : msg})



def register_user(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        fname = request.POST['fname']
        lname = request.POST['lname']
        try:
            if User.objects.filter(username = username).first():
                msg = "Username Already Taken"
                messages.error(request, "Username Already Taken")
                return render(request, 'authenticate/register.html', {"msg" : msg})
            elif User.objects.filter(email = email).first():
                msg = "Email Already Registered"
                messages.warning(request, "Email Already Registered")
                return render(request, 'authenticate/register.html', {"msg" : msg})
            elif password != password2:
                msg = "Password Not Matched"
                messages.warning(request, "Password Not Matched")
                return render(request, 'authenticate/register.html', {"msg" : msg})
            elif len(password) < 8:
                msg = "Please Select A Strong Password Minimum 8 Character."
                messages.warning(request, "Please Select A Strong Password Minimum 8 Character")
                return render(request, 'authenticate/register.html', {"msg" : msg})
            else:
                u = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
                u.save()
                return redirect('/login/')

        except Exception as e:
            msg = f"Error Please Try Again..... {e[:36]}..."
            messages.error(request, f"Error Please Try Again..... Error: {e[:36]}...")
            return render(request, 'authenticate/register.html', {"msg" : msg})

    elif request.method!='POST':
        msg = "Please Fill The Registration Form"
        messages.info(request, "Please Fill The Registration Form")
        return render(request, 'authenticate/register.html', {"msg" : msg})
    
    else:
        msg = "Error Please Try Again"
        messages.warning(request, "Password Not Matched")
        return render(request, 'authenticate/register.html', {"msg" : msg})

def logout_view(request):
    logout(request)
    return redirect('/')


def del_user(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            if User.objects.filter(username=username).first():
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    u = User.objects.get(username=username)
                    u.delete()
                    return redirect('/register')
                else:
                    msg = "Password Not Matched"
                    messages.warning(request, "Password Not Matched")
                    return render(request, 'authenticate/delete.html', {"msg" : msg})
                    
            else:
                msg = "User Doesn't Exist"
                messages.error(request, "User Doesn't Exist")
                return render(request, 'authenticate/delete.html', {"msg" : msg})
            
        except User.DoesNotExist:
            msg = "User Doesn't Exist"
            messages.error(request, "User Doesn't Exist")
            return render(request, 'authenticate/delete.html', {"msg" : msg})

        except Exception as e: 
            msg = f"Error Please Try Again..... Error: {e[:36]}..."
            messages.error(request, f"Error Please Try Again..... Error: {e[:36]}...")
            return render(request, 'authenticate/delete.html', {"msg" : msg})
    
    elif request.method!='POST':
        msg = "Delete Your Account"
        # messages.error(request, "ERROR: Delete Your Account")
        # messages.success(request, "SUCCESS: Delete Your Account")
        # messages.info(request, "INFO: Delete Your Account")
        messages.warning(request, "Delete Your Account")
        return render(request, 'authenticate/delete.html', {"msg" : msg})
        
    else:
        msg = "Error Please Try Again"
        messages.error(request, "Error Please Try Again")
        return render(request, 'authenticate/delete.html', {"msg" : msg})