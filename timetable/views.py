from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'timetable/base.html', {"weeks":range(4),"first_day":3,"month_lenght":30})
