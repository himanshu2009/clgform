
from django.shortcuts import render

from django.template import loader
from django.urls import reverse

from django.http import HttpResponseRedirect, HttpResponse
import json
import os

from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from django .contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm


# deparment page view logic
def department(request):

    return render(request, 'enroll/department.html')


# cse ke form ka logic
def cse(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    cse_subjects = data["Computer Science and Engineering"]

    return render(request, './enroll/cse.html', {'data': cse_subjects})


def chemical(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    entc_subjects = data["Electronics and telecommunication"]
    # biodata= {'name':"himanshu"}

    return render(request, 'enroll/entc.html', {'data': entc_subjects})

    return render(request, './enroll/chemical.html')


def civil(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    entc_subjects = data["Electronics and telecommunication"]
    # biodata= {'name':"himanshu"}

    return render(request, 'enroll/entc.html', {'data': entc_subjects})

    return render(request, './enroll/civil.html')


def entc(request):
    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    entc_subjects = data["Electronics and telecommunication"]
    # biodata= {'name':"himanshu"}

    return render(request, 'enroll/entc.html', {'data': entc_subjects})


def mech(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    entc_subjects = data["Electronics and telecommunication"]
    # biodata= {'name':"himanshu"}

    return render(request, 'enroll/entc.html', {'data': entc_subjects})

    


def electrical(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    entc_subjects = data["Electronics and telecommunication"]
    # biodata= {'name':"himanshu"}

    return render(request, 'enroll/entc.html', {'data': entc_subjects})



def it(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    it_subjects = data["Information Technology"]
    # biodata= {'name':"himanshu"}

    return render(request, 'enroll/entc.html', {'data': it_subjects})




def production(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    entc_subjects = data["Electronics and telecommunication"]
    # biodata= {'name':"himanshu"}

    return render(request, 'enroll/entc.html', {'data': entc_subjects})

    return render(request, './enroll/production.html')


def textile(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    entc_subjects = data["Electronics and telecommunication"]
    # biodata= {'name':"himanshu"}

    return render(request, 'enroll/entc.html', {'data': entc_subjects})

    return render(request, './enroll/textile.html')


def instru(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    #   passing cse subjects
    entc_subjects = data["Electronics and telecommunication"]
    # biodata= {'name':"himanshu"}

    return render(request, 'enroll/entc.html', {'data': entc_subjects})

    return render(request, './enroll/instru.html')


# registration logic

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'enroll/signup.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
        return render(request, 'enroll/signup.html', {'form': form})


# login function

def user_login(request):

    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)

        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, passord=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('profile')
    else:
        fm = AuthenticationForm()
    return render(request, 'enroll/userlogin.html', {'form': fm})


# profile


@login_required
def user_profile(request):
    user = request.user
    return render(request, 'enroll/profile.html', {'user': user})


@login_required
def home(request):
    return render(request, 'enroll/home.html')


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'path/to/email/template.html'
    form_class = CustomPasswordResetForm
