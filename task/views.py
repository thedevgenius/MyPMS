from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def TaskDispaly(request):
    theme = request.session.get('inlineRadioOptions')
    tasks = Task.objects.filter(assigned_to=request.user.id).order_by('priority')

    data = {
        'theme' : theme,
        'tasks' : tasks
    }
    return render(request, 'task.html', data)

@login_required
def TaskDetails(request, id):
    theme = request.session.get('inlineRadioOptions')
    tasks = Task.objects.filter(assigned_to=request.user.id)
    task = get_object_or_404(Task, id=id)
    users = Member.objects.all()
    commemts = Commemts.objects.filter(task_id=id)

    data = {
        'theme' : theme,
        'tasks' : tasks,
        'task' : task,
        'users' : users,
        'commemts' : commemts
    }
    return render(request, 'task-details.html', data)

@login_required
def ChangeAssign(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        new_id = request.POST['assignes']
        task.assigned_to = Member.objects.get(pk=new_id)
        task.save()
        return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def AddComment(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        member = get_object_or_404(Member, id=request.user.id)
        description = request.POST['comments']
        Commemts.objects.create(
            task=task,
            member=member,
            description=description
        )
        return redirect(request.META.get('HTTP_REFERER', 'home'))    

