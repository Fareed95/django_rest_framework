from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('employee', views.Employeelistview, name = 'employee'),
    path ('users', views.userlistview, name = 'users')
]
