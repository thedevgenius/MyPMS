from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def Home(request):
    theme = request.session.get('inlineRadioOptions')
    return render(request, 'index.html', {'theme' : theme})


def Theme(request):
    if request.method == 'POST':
        theme = request.POST['inlineRadioOptions']
        request.session['inlineRadioOptions'] = theme
    return redirect(request.META.get('HTTP_REFERER', 'home'))