from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('logout/',views.logout_view,name='logout'),
    path('add_department/',views.add_department,name='add_department'),
    path('department_list/',views.department_list,name="department_list"),
    path('department/<int:dept_id>/', views.department_detail, name='department_detail'),
    path(
    'department/<int:dept_id>/add-employee/',
    views.add_employee_by_dept,
    name='add_employee_by_dept'),

]