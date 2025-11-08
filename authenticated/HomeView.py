from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required
def home_view_get(request):
    if request.method == 'GET':
        

        return render(request,'authenticated/home.html')