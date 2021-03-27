from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.models import User
from .models import Profile, Chat
from .forms import LoginForm, UserForm

# Create your views here.
def index(request):
    return render(request, "Chats/index.html", {})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return redirect('/error/')
    else:
        form = LoginForm()

    context = {
            'form': form,
            'active_tab': 'login',
            }
    return render(request, "Chats/login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("/")

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # save user
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            bio = form.cleaned_data['bio']

            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            profile = Profile(user=user, bio=bio)

            profile.save()
            user.save()
            auth_login(request, user)

            return redirect('/')
    else:
        form = UserForm()

    context = {
            'form': form,
            'active_tab': 'new_user',
            }
    return render(request, "Chats/new_user.html", context)


def error(request):
    return HttpResponse("Error: you made a mistake")
