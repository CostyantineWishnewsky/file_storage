from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied



from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from guest.validation.LoginForm import LoginForm

User = get_user_model()

def login_view_get(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
    
        return render(request,'guest/login.html')

def login_view_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('home')
        form=LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(email=form.cleaned_data['email'])
            if user is None:
                return HttpResponseForbidden("403 Forbidden: Access denied.")

            if user.check_password(form.cleaned_data['password']):
                login(request,user)
                return redirect('home')
            return HttpResponseForbidden("403 Forbidden: Access denied.")
        return HttpResponseForbidden("403 Forbidden: Access denied.")