from django.urls import path

from guest.LoginView import login_view_get,login_view_post

urlpatterns = [
    # path('',LoginView.as_view()),
    path('',login_view_get,name='login'),
    path('login/',login_view_post)
    # path('login/',LoginView.post),
]
