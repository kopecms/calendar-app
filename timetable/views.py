from django.shortcuts import render

from django.http import HttpResponse
from django.utils.safestring import mark_safe
from calendar_generator import Calendar
from django.shortcuts import render_to_response
def index(request):
  year = 2016
  month = 12
  cal = Calendar().formatmonth(year, month)
  cal = cal.split("\n",1)[1]
  cal = '<table class="table table-bordered">\n'+cal
  return render_to_response('timetable/base.html', {'calendar': mark_safe(cal),})
