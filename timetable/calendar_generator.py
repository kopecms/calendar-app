from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape as esc
import datetime
def create_calendar():
    year = datetime.date.today().year
    month = datetime.date.today().month

    cal = Calendar().formatmonth(year, month)
    cal = cal.split("\n",1)[1]
    cal = '<table class="table table-bordered">\n'+cal
    return mark_safe(cal)

class Calendar(HTMLCalendar):

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(Calendar, self).formatmonth(year, month)

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)
