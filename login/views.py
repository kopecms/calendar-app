from django.shortcuts import render, render_to_response
from django.template import  RequestContext
# Create your views here.
from login.forms import UserForm, UserProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login
from timetable.calendar_generator import create_calendar

from django.views.decorators.csrf import ensure_csrf_cookie
from timetable.forms import TaskForm
from timetable.views import index

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@ensure_csrf_cookie
def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            return index(request)

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        }
    return render(request,
            'login/register.html',  context)
