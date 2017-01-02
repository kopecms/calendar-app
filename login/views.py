from django.shortcuts import render, render_to_response
from django.template import  RequestContext
# Create your views here.
from login.forms import UserForm, UserProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login

# use if request.method == 'POST'
def user_login_validation(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Your Rango account is disabled.")
    else:
            return HttpResponse("Invalid login details supplied.")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    context = RequestContext(request)
    registered = False

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
            registered = True
            return render_to_response('timetable/home.html', {'calendar': "" }, context)
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'login/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)
