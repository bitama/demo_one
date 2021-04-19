from django.shortcuts import render,redirect
from .models import Department,Employee

def index(request):
    context={
    "departments":Department.objects.all()
    }
    return render(request,"index.html",context)


def create_user(request):
    if request.POST["department_id"]=="-1":
        department=Department.objects.create(name=request.POST["department_name"])
    # else:
    #     department=Department.objects.get(id=request.POST["department_id"])
    
    Employee.objects.create(
        first_name=request.POST["first_name"],
        middle_name=request.POST["middle_name"],
        last_name=request.POST["last_name"],
        salary=request.POST["salary"],
        department=Department.objects.get(id=request.POST["department_id"])
    )
    return redirect("/")
def employee_info(request,employee_id):
    context ={
        "employee":Employee.objects.get(id=employee_id)
    }
    return render(request,"info.html",context)

def delete_employee(request,employee_id):
    
    Employee.objects.get(id=employee_id).delete()
    return redirect('/')
    
def edit_employee(request,employee_id):
    context ={
        "employee":Employee.objects.get(id=employee_id),
        "departments":Department.objects.all()
    }
    return render(request,"edit.html",context)

def update_employee(request,employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.first_name=request.POST["first_name"]
    employee.middle_name=request.POST["middle_name"]
    employee.last_name=request.POST["last_name"]
    employee.salary=request.POST["salary"]
    employee.department=Department.objects.get(id=request.POST["department_id"])
    employee.save()
    return redirect(f"/employees/{employee_id}")
        