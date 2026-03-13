from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils.timezone import now


# READ
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# CREATE
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})


# UPDATE
def edit_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form})


# DELETE
def delete_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect('task_list')


# SEARCH
def search_task(request):

    query = request.GET.get('q')

    tasks = Task.objects.filter(title__icontains=query)

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def dashboard(request):

    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(status="Completed").count()

    pending_tasks = Task.objects.filter(status="Pending").count()

    overdue_tasks = Task.objects.filter(
        due_date__lt=now().date(),
        status="Pending"
    ).count()

    context = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "overdue_tasks": overdue_tasks,
    }

    return render(request, "tasks/dashboard.html", context)

def task_list(request):

    filter_type = request.GET.get('filter')

    if filter_type == "pending":
        tasks = Task.objects.filter(status="Pending")

    elif filter_type == "completed":
        tasks = Task.objects.filter(status="Completed")

    elif filter_type == "overdue":
        tasks = Task.objects.filter(
            due_date__lt=now().date(),
            status="Pending"
        )

    else:
        tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }

    return render(request, "tasks/task_list.html", context)

def task_list(request):

    filter_type = request.GET.get('filter')

    if filter_type == "pending":
        tasks = Task.objects.filter(status="Pending")

    elif filter_type == "completed":
        tasks = Task.objects.filter(status="Completed")

    elif filter_type == "overdue":
        tasks = Task.objects.filter(
            due_date__lt=now().date(),
            status="Pending"
        )

    else:
        tasks = Task.objects.all()

    context = {
        "tasks": tasks,
        "today": now().date()
    }

    return render(request, "tasks/task_list.html", context)