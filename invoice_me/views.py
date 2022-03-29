from django import http
from django.shortcuts import render, redirect
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


@login_required(login_url='login')
def landing_page(request):

    return render(request, 'landing_page.html')

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("hello")
            return redirect('landing_page')
        else:
            messages.error(request, 'Invalid login credenntials')
            
            return redirect('login')
    
    return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):

    auth.logout(request)

    return redirect('login')

@login_required(login_url='login')
def change_password(request):

    user = User.objects.get(username__exact = request.user.username)

    if request.method == 'POST':

        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        success = user.check_password(old_password)

        if success:
            if new_password == confirm_password:
                user.set_password(new_password)
                update_session_auth_hash(request, user)
                user.save()
                messages.error(request, "password changed successfully")
                return redirect('change_password')
            else:
                messages.error(request, "password mismatch")
                return redirect('change_password')

        else:
            messages.error(request, "invalid old password")
            return redirect('change_password')
    return render(request, 'change_password.html')



