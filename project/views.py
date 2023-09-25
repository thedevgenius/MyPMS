from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

@login_required
def Projects(request):
    theme = request.session.get('inlineRadioOptions')
    project = Project.objects.all().order_by('title')
    
    data = {
        'project' : project,
        'theme' : theme
    }
    return render(request, 'project.html', data)



@login_required
def ProjectDetails(request, slug):
    theme = request.session.get('inlineRadioOptions')
    projects = get_object_or_404(Project, slug=slug)
    files = File.objects.filter(project_id=projects.id)
    
    data = {
        'theme' : theme,
        'projects' : projects,
        'files' : files
    }
    return render(request, 'project-details.html', data)

@login_required
def ProjectEdit(request, id):
    theme = request.session.get('inlineRadioOptions')
    post = get_object_or_404(Project, pk=id)
    if post.associate_id != request.user.id:
        return redirect('project')
    
    if request.method == 'POST':
        form = ProjectEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ProjectEditForm(instance=post)

    data = {
        'theme' : theme,
        'form' : form,
        'post' : post
    }
    return render(request, 'project-edit.html', data)

# @login_required
# def Files(request):
#     theme = request.session.get('inlineRadioOptions')
#     files = File.objects.all()

#     data = {
#         'theme' : theme,
#         'files' : files
#     }
#     return render(request, 'files.html', data)

@login_required
def AddFiles(request, id):
    theme = request.session.get('inlineRadioOptions')
    if request.method == 'POST':
        files = request.FILES.getlist('projectfiles')
        project_id = id
        for file in files:
            File.objects.create(
                file = file,
                project_id = project_id
            )
        return redirect('project')


    data = {
        'theme' : theme,
    }
    return render(request, 'add-files.html', data)