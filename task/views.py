from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def TaskDispaly(request):
    theme = request.session.get('inlineRadioOptions')
    tasks = Task.objects.filter(assigned_to_id=request.user.id)

    data = {
        'theme' : theme,
        'tasks' : tasks
    }
    return render(request, 'task.html', data)

def TaskDetails(request, id):
    theme = request.session.get('inlineRadioOptions')
    tasks = Task.objects.filter(assigned_to_id=request.user.id)
    task = get_object_or_404(Task, id=id)
    users = Member.objects.all()

    data = {
        'theme' : theme,
        'tasks' : tasks,
        'task' : task,
        'users' : users
    }
    return render(request, 'task-details.html', data)


def ChangeAssign(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        new_id = request.POST['assignes']
        task.assigned_to = Member.objects.get(pk=new_id)
        task.save()
        return redirect('task')
    
