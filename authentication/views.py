from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Register

def register(request):

    if request.method == 'POST':
        username = request.POST[ 'username']
        password1 = request.POST[ 'password1']
        password2 = request.POST[ 'password2']
        first_name = request.POST[ 'first_name']
        last_name = request.POST[ 'last_name']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email ID Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user (password=password1, email=email,username=username,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/register')
    else:   
        return render(request, 'base/register.html')

# Login

def login(request):

    if request.method == 'POST':
        username = request.POST[ 'username']
        password = request.POST[ 'password']

        user = auth.authenticate (password=password,username=username)

        if user is not None:
            auth.login(request, user)
            return redirect("/create")
        else:
            messages.info(request,'Check your username and password')
            return redirect('login')   
    else:
        return render(request,'base/login.html')

# Logout

def logout(request):
    auth.logout(request)
    return redirect("/create")


