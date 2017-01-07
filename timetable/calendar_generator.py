from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape as esc
import datetime

from django.contrib.auth.models import User
from .models import TasksPerDay

def create_calendar(request, year = datetime.date.today().year, month = datetime.date.today().month):
    if  request.user.is_authenticated():
        tasks_per_day = TasksPerDay.objects.order_by('date').filter(owner = request.user,
                    date__year=year, date__month=month
                    )
    else:
        tasks_per_day = TasksPerDay.objects.order_by('date').filter(owner=User.objects.get(username="exampleUser"),
                    date__year=year, date__month=month
                    )
    cal = Calendar(tasks_per_day).formatmonth(year, month)
    cal = cal.split("\n",1)[1]
    cal = '<table class="table table-bordered">\n'+cal
    print(cal)
    return mark_safe(cal)

def date_info_dict(year = datetime.date.today().year, month = datetime.date.today().month):
    date = {}

    date["today"] = datetime.date.today().day
    date["month"] = month
    date["year"] = year

    calendar_at_date = datetime.date(year,month,1)
    previous_month_date = calendar_at_date - datetime.timedelta(days=1)
    previous_month = previous_month_date.month
    previous_year = previous_month_date.year

    next_month_date = calendar_at_date + datetime.timedelta(days=31)
    next_month = next_month_date.month
    next_year = next_month_date.year

    date["previous_month"] = previous_month
    date["previous_year"] = previous_year
    date["next_month"] = next_month
    date["next_year"] = next_year

    return date
def month_to_num(month):
    return{
        'January' : 1,
        'February' : 2,
        'March' : 3,
        'April' : 4,
        'May' : 5,
        'June' : 6,
        'July' : 7,
        'August' : 8,
        'September' : 9,
        'October' : 10,
        'November' : 11,
        'December' : 12
    }[month]

class Calendar(HTMLCalendar):
    def __init__(self, tasks):
        super(Calendar, self).__init__()
        self.tasks = self.group_by_day(tasks)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.tasks:
                cssclass += ' ' + str(day)
                body = ['<span class="badge pull-right">']
                for task in self.tasks[day]:
                    body.append(esc(task.number))
                body.append('</span>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(Calendar, self).formatmonth(year, month)

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

    def group_by_day(self, tasks):
        field = lambda tasks: tasks.date.day
        return dict(
            [(day, list(items)) for day, items in groupby(tasks, field)]
        )
