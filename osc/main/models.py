from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


SIGNAL_SOURCES = (
    ('SOUR1', 'Source 1'),
    ('SOUR2', 'Source 2')
)

SIGNAL_FORMS = (
    ('SIN', 'Гармонический'),
    ('SQU', 'Меандр'),
    ('RAMP', 'Треугольный')
)


class SignalGenerator(models.Model):
    channel = models.CharField(max_length=50, choices=SIGNAL_SOURCES)
    sig_form = models.CharField(max_length=50, choices=SIGNAL_FORMS)
    frequency = models.FloatField(
        default=10000,
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(100000)
        ]
    )
    amplitude = models.FloatField(
        default=12,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(18)
        ]
    )


class Oscilloscope(models.Model):
    ch_scale = models.FloatField(
        default=0.2,
        validators=[
            MinValueValidator(0.0001),
            MaxValueValidator(1)
        ]
    )
    time_base = models.FloatField(
        default=0.0002,
        validators=[
            MinValueValidator(0.000001),
            MaxValueValidator(0.1)
        ]
    )


    def __str__(self):
        return self.channel
