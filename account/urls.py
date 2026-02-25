from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('employees/add/',views.add_employee,name='add_employee'),
    path('employees/',views.employee_list,name='employee_list'),
    path('logout/',views.logout_view,name='logout')
    ]