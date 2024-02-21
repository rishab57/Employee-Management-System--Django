from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import EmpForm
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def view(request):
    employees = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request, 'view-all.html', context)

def create(request):
    form = EmpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': 'form'
    }
    return redirect(request, 'create-emp', context)
    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     desc = request.POST['desc']
    #     salary = int(request.POST['salary'])
    #     bonus = int(request.POST['bonus'])
    #     role = request.POST['role']
    #     phone = request.POST['phone']
    #     new_emp = Employee(first_name = first_name, last_name = last_name, desc_id = desc, salary = salary, bonus = bonus, role_id = role, phone = phone, doj = datetime.now())
    #     new_emp.save()
    #     return HttpResponse("Employee record Added Succesfully.")
    # else:
    #     return HttpResponse("An Exception Occured...plz try again.....😶‍🌫️😶‍🌫️")

def delete(request, emp_id = 0):
    if emp_id:
        try: 
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")    
        except:
            return HttpResponse("plz enter a valid Employee Id")    

    employees = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request, 'delete-emp.html',context )

def filter(request):
    
    return render(request, 'filter-emp.html')
