from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('employee', views.Employeelistview, name = 'employee'),
    path('employee/<int:pk>', views.EmployeeDetailView, name = 'EmployeeDetailView'),
    path ('users', views.userlistview, name = 'users')
]
