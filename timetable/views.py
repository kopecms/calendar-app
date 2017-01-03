from django.shortcuts import render

from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.template import  RequestContext
from timetable.calendar_generator import Calendar

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from login.views import user_login_validation
import json

from .forms import TaskForm

from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Task
def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Task(text=post_text, owner=request.user)
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
    year = 2016
    month = 12
    cal = Calendar().formatmonth(year, month)
    cal = cal.split("\n",1)[1]
    cal = '<table class="table table-bordered">\n'+cal
    print (cal)
    form = TaskForm()
    if request.method == 'POST':
        return user_login_validation(request)
    else:
        return render(request, 'timetable/home.html', {'form':form,'calendar': mark_safe(cal), })
