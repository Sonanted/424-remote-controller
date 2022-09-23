from django.shortcuts import render, redirect
from .models import Oscilloscope, SignalGenerator
from .forms import ScopeForm, GeneratorForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

import pyvisa
import matplotlib.pyplot as plot
import math
import numpy
import time as timee

# import warnings
# warnings.filterwarnings("ignore")

from io import StringIO

def mod_appliances(request):
    rm = pyvisa.ResourceManager()
    scope_usb = list(filter(lambda x: 'DS1ZD204101021' in x, rm.list_resources()))
    generator_usb = list(filter(lambda x: 'DG1ZA202603185' in x, rm.list_resources()))
    scope = rm.open_resource(scope_usb[0])
    generator = rm.open_resource(generator_usb[0])
    generator.write(f'{request["channel"]}:APPL:{request["sig_form"]} {request["frequency"]},{request["amplitude"]}')
    scope.write(":RUN")
    scope.write(f':TIMebase:SCALe {request["time_base"]}')
    scope.write(f':CHANnel1:SCALe {request["ch_scale"]}')
    timee.sleep(0.5)
    scope.write(":STOP")
    
    scope.close()


def return_graph():
    rm = pyvisa.ResourceManager()
    scope = rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZD204101021::INSTR')
    scope.write(":RUN")
    timee.sleep(2)
    scope.write(":STOP")
    sample_rate = scope.query_ascii_values(':ACQ:SRAT?')[0]
    scope.write(":WAV:SOUR CHAN1")
    YORigin = scope.query_ascii_values(":WAV:YOR?")[0]
    YREFerence = scope.query_ascii_values(":WAV:YREF?")[0]
    YINCrement = scope.query_ascii_values(":WAV:YINC?")[0]
    XORigin = scope.query_ascii_values(":WAV:XOR?")[0]
    XREFerence = scope.query_ascii_values(":WAV:XREF?")[0]
    XINCrement = scope.query_ascii_values(":WAV:XINC?")[0]
    time_base = scope.query_ascii_values(":TIM:SCAL?")[0]
    memory_depth = (time_base*12) * sample_rate
    scope.write(":WAV:MODE RAW")
    scope.write(":WAV:FORM BYTE")
    scope.write(":WAV:STAR 1")
    scope.write(":WAV:STOP 250000")
    rawdata = scope.query_binary_values(":WAV:DATA?", datatype='B')
    if (memory_depth > 250000):
        loopcount = 1
        loopmax = math.ceil(memory_depth/250000)
        while (loopcount < loopmax):
            start = (loopcount*250000)+1
            scope.write(":WAV:STAR {0}".format(start))
            stop = (loopcount+1)*250000
            scope.write(":WAV:STOP {0}".format(stop))
            rawdata.extend(scope.query_binary_values(":WAV:DATA?", datatype='B'))
            loopcount = loopcount+1
    scope.write(":MEAS:SOUR CHAN1")
    scope.close()
    data = (numpy.asarray(rawdata) - YORigin - YREFerence) * YINCrement
    data_size = len(data)
    time = numpy.linspace(XREFerence, XINCrement * data_size, data_size)
    if (time[-1] < 1e-3):
        time = time * 1e6
        tUnit = "uS"
    elif (time[-1] < 1):
        time = time * 1e3
        tUnit = "mS"
    else:
        tUnit = "S"
    fig = plot.figure()
    plot.plot(time, data)
    plot.ylabel("Voltage (V)")
    plot.xlabel("Time (" + tUnit + ")")
    plot.grid()
    plot.xlim(time[0], time[-1])
    plot.subplots_adjust(left=0.1,top=0.98,bottom=0.1,right=0.8)
    # plot.show()
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data

def home_page(request):
    return render(request, 'main/index.html')


class Scope(View):
    def get(self, request):
        print('get')
        form = ScopeForm()
        form2 = GeneratorForm()
        context = {
            'form': form,
            'form2': form2
            }
        return render(request, 'main/scope.html', context=context)

    def post(self, request):
        print('post')
        form = ScopeForm(request.POST)
        form2 = GeneratorForm(request.POST)
        context = {
            'form': form,
            'form2': form2
            }
        if form.is_valid() and form2.is_valid():
            mod_appliances(request.POST)
            context['graph'] = return_graph()
        return render(request, 'main/scope.html', context=context)


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
