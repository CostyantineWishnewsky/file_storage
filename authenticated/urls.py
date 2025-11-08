from django.urls import path

# from authenticated.HomeView import HomeView
from authenticated.HomeView import home_view_get
from authenticated.LoginView import login_view_delete

urlpatterns = [
    # path('/',HomeView.as_view(),name='home'),
    path('',home_view_get,name='home'),
    path('logout',login_view_delete),
    # path('login/',LoginView.post),
]
