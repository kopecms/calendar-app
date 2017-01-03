from django.shortcuts import render

from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.template import  RequestContext
from timetable.calendar_generator import create_calendar

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from login.views import user_login_validation
import json

from .forms import TaskForm

from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Task
import datetime
from django.core.exceptions import ObjectDoesNotExist

def get_day(request):
    if request.method == 'GET':
        task_day = request.GET.get("task_day")

        response_data = {}

        try:
            tasks = Task.objects.filter(date=task_day)
            for idx, task in enumerate(tasks):
                response_data["task"+str(idx)] = task.text
        except ObjectDoesNotExist:
            response_data["task0"] = "No tasks"
        finally:
            pass

        response_data['result'] = 'Create post successful!'

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

        post = Task(text=post_text, date = post_day, owner=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['owner'] = post.owner.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


@ensure_csrf_cookie
def index(request):

    form = TaskForm()
    if request.method == 'POST':
        return user_login_validation(request)
    else:
        return render(request, 'timetable/home.html', {'form':form,'calendar': create_calendar(), })
