from django.shortcuts import render

from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.template import  RequestContext
from timetable.calendar_generator import create_calendar

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
import json
from .calendar_generator import date_info_dict

from timetable.forms import TaskForm
from login.forms import LoginForm

from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Task
import datetime
from django.core.exceptions import ObjectDoesNotExist

def get_day(request):
    if request.method == 'GET':
        task_day = request.GET.get("task_day")

        response_data = {}
        try:
            tasks = Task.objects.filter(date=task_day, owner=request.user)
            for idx, task in enumerate(tasks):
                response_data["task"+str(idx)] = task.text
        except:
            pass

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def create_task(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        post_day =  request.POST.get('the_day')

        response_data = {}
        try:
            post = Task(text=post_text, date = post_day, owner=request.user)
            post.save()

            response_data['result'] = 'Create post successful!'
            response_data['postpk'] = post.pk
            response_data['text'] = post.text
            response_data['owner'] = post.owner.username
        except:
            return HttpResponse(
                json.dumps({"text": "Log in to add tasks"}),
                content_type="application/json")

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json")

def other_month(request, year, month):
    context = {
        'task_form' : TaskForm(),
        'login_form' : LoginForm(),
        'calendar' : create_calendar(int(year),int(month)),
        'date' : date_info_dict(int(year),int(month)),
    }
    return render(request, 'timetable/home.html', context)

@ensure_csrf_cookie
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                context = {
                'task_form' : TaskForm(),
                'calendar' : create_calendar() ,
                'date' : date_info_dict(),
            }
                return render(request, 'timetable/home.html', context)
            else:
                return HttpResponse("Your account is disabled.")
        else:
                return HttpResponse("Invalid login details supplied.")
    else:
        context = {
            'task_form' : TaskForm(),
            'login_form' : LoginForm(),
            'calendar' : create_calendar(),
            'date' : date_info_dict(),
        }
        return render(request, 'timetable/home.html', context)
