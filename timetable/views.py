from django.shortcuts import render

from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.template import  RequestContext
from timetable.calendar_generator import Calendar

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from login.views import user_login_validation

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def index(request):
    year = 2016
    month = 12
    cal = Calendar().formatmonth(year, month)
    cal = cal.split("\n",1)[1]
    cal = '<table class="table table-bordered">\n'+cal

    context = RequestContext(request)

    if request.method == 'POST':
        return user_login_validation(request)
    else:
        return render_to_response('timetable/home.html', {'calendar': mark_safe(cal), }, context)
