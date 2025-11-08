from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def login_view_delete(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')