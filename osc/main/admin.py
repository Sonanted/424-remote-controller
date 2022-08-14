from django.contrib import admin
from .models import Oscilloscope, SignalGenerator

admin.site.register(Oscilloscope)
admin.site.register(SignalGenerator)