from django.db import models


SIGNAL_SOURCES = (
    ('SOUR1', 'Source 1'),
    ('SOUR2', 'Source 2')
)

SIGNAL_FORMS = (
    ('SIN', 'Синусоида'),
    ('SQU', 'Меандр'),
    ('RAMP', 'Треугольный')
)


class SignalGenerator(models.Model):
    channel = models.CharField(max_length=20, choices=SIGNAL_SOURCES)
    sig_form = models.CharField(max_length=20, choices=SIGNAL_FORMS)
    frequency = models.CharField(max_length=20)
    amplitude = models.CharField(max_length=20)


class Oscilloscope(models.Model):
    ch_scale = models.CharField(verbose_name='ch_scale', max_length=12, default="200m")
    time_base = models.CharField(verbose_name='time_base', max_length=12, default="200u")


    def __str__(self):
        return self.channel
