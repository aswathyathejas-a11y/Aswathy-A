from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Employee,Department
from .forms import EmployeeForm,DepartmentForm

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    return render(request,'login.html')
@login_required
def dashboard_view(request):
    return render(request,'dashboard.html')

@login_required

def add_employee_by_dept(request, dept_id):
    department = Department.objects.get(id=dept_id)

    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        employee = form.save(commit=False)
        employee.department = department
        employee.save()
        return redirect('department_detail', dept_id=dept_id)

    return render(request, 'add_employee.html', {
        'form': form,
        'department': department
    })
@login_required

def add_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('department_list')

    return render(request, 'add_department.html', {'form': form})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {
        'departments': departments
    })
def department_detail(request, dept_id):
    department = Department.objects.get(id=dept_id)
    employees = department.employees.all()

    return render(request, 'department_detail.html', {
        'department': department,
        'employees': employees
    })

def logout_view(request):
    logout(request)
    return redirect('login')
