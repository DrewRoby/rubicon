from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Library
from cons.models import Con
from datetime import datetime as dt


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check password match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'An account already exists for that email')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    auth.login(request, user)
                    ConName = f"{username}'s Own Private Idaho"
                    ConTag = "Your personal game history.  Invite others to begin playing."
                    ConOwner = username
                    Begin = dt.now()
                    End = None
                    Con.objects.create(CON_NAME=ConName, CON_TAGLINE=ConTag, CON_OWNER=ConOwner, CON_BEGIN=Begin, CON_END=End, CREATE_DATE=Begin, IS_PRIVATE=True)
                    messages.success(request, 'Welcome to Rubicon!')

                    return redirect('dashboard')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'players/register.html')

def login(request):
    if request.method == 'POST':
        # login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'players/login.html')

def logout(request):
    return render(request,'index')

def dashboard(request):
    # check user is logged in
    # if not request.user:
    #     return redirect('login.html')

    # link current user to library
    user = request.user
    libgames = Library.objects.filter(username=user.id)


    context = {
        "numgames": len(libgames),
        "tag": user.username,
        "userrealname": user.first_name + " " + user.last_name
    }
    return render(request,'players/dashboard.html',context)