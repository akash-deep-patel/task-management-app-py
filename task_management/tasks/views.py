from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if 'clear_tasks' in request.POST:
            Task.objects.all().delete()
            return redirect('home')
        else:
            form = TaskForm(request.POST)
            if not request.POST.get('name') or not request.POST.get('category'):
                return render(request, 'tasks/home.html', {'form': form, 'tasks': Task.objects.all(), 'error': 'Name and category cannot be blank.'})
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'form': form, 'tasks': tasks})
