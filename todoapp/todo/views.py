from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone
# Create your views here.

def home(request):
    tasks = Task.objects.filter(completed=False)
    completed_tasks = Task.objects.filter(completed=True) 
    context ={
        "tasks": tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'todo/home.html', context)


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
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm( request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {
        # 'task': task,
        'form': form,
    }
    return render(request, 'todo/editTask.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'todo/deleteTask.html', {'obj': pk})

def todayTask(request):
    today = timezone.now().date()
    tasks = Task.objects.filter(deadline__date=today, completed=False)
    completed_tasks = Task.objects.filter(completed=True) 
    context ={
        "tasks": tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'todo/today.html', context)


def pendingTask(request):
    now = timezone.now()
    tasks = Task.objects.filter( completed=False)
    completed_tasks = Task.objects.filter(completed=True)
    context ={
        "tasks": tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'todo/pending.html', context)

def overdueTask(request):
    now = timezone.now()
    tasks = Task.objects.filter(deadline__date__lt=now, completed=False)
    completed_tasks = Task.objects.filter(completed=True)
    context ={
        "tasks": tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'todo/overdue.html', context)


def completedTask(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'completed.html', {'tasks':tasks})

def toggle_completed(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        task.completed = not task.completed
        # return redirect(request.META.get("HTTP_REFERER", "completed"))
        task.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))