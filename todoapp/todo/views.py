from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'todo/home.html', {'tasks':tasks })


def createTask(request):
    tasks = Task.objects.all()  
    if request.method == 'POST':
        form = TaskForm(request.POST)   
        if form.is_valid():             
            form.save()                 
            return redirect('home')     
    else:
        form = TaskForm()               
    context = {'tasks': tasks, 'form': form}

    return render(request, 'todo/createTask.html', context)

def editTask(request, pk):
    task = Task.objects.get(
        id=pk
    )
    task = Task
    return render(request, 'todo/edit.html')

def deleteTask(request, pk):
    return render(request, 'todo/edit.html')

def today(request):
    return render(request, 'todo/today.html')


def pending(request):
    return render(request, 'todo/pending.html')

def overude(request):
    return render(request, 'todo/overdue.html')