from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('create_employee/', views.create_employee, name='create_employee'),
    path('signout/', views.signout, name='signout'),
    path('timespend/', views.timespend, name='timespend'),

]