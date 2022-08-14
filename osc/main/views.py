from django.shortcuts import render, redirect
from .models import Oscilloscope, SignalGenerator
from .forms import ScopeForm, GeneratorForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .tests import desktop_app_usage

# import warnings
# warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

def mod_appliances():
    pass

def create_result():
    pass

def return_graph():

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def home_page(request):
    return render(request, 'main/index.html')


class Scope(View):
    def get(self, request):
        form = ScopeForm()
        form2 = GeneratorForm()
        context = {
            'form': form,
            'form2': form2
            }
        
        context['graph'] = return_graph()
        return render(request, 'main/scope.html', context=context)

    def post(self, request):
        form = ScopeForm(request.POST)
        form2 = GeneratorForm(request.POST)
        if form.is_valid() and form2.is_valid():
            username = request.user.username
            filename = 'osc'
            print(form.cleaned_data)
            print(form2.cleaned_data)
            mod_appliances()
            return redirect('scope')
            # return JsonResponse({'url': "{% static 'main/" + filename + ".png' %}"}, status=200)
        else:
            print('Not valid')
            print(form.cleaned_data)
            print(form2.cleaned_data)
            return redirect('scope')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {'form': AuthenticationForm}
    return render(request, 'main/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')


def reset_page(request):
    return redirect('home')


def donut_page(request):
    return render(request, 'main/donut.html')
