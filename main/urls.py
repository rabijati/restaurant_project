from django.urls import path

from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",index,name='index'),
    path("about/",about,name='about'),
    path("services/",services,name='services'),
    path("menu/",menu,name='menu'),
    path("contact/",contact,name='contact'),

    #auth part------------------------------
    path("register/",register, name="register"),
    path("login/",log_in, name="log_in"),
    path("logout/",log_out, name="log_out"),  

    # password related change and forgot password 
    path("change_password",change_password, name="change_password"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),


  
    path("split/", split, name="split")


]

