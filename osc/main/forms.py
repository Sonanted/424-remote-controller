from .models import Oscilloscope, SignalGenerator
from django.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


# not used because it doesn't actually style forms
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                'type': 'text',
                'id': 'username',
                'class': 'form-control',
                'placeholder': 'username',
                'required': 'required',
                'autofocus': 'autofocus'
            }),
            "password": PasswordInput(attrs={
                'type': 'password',
                'id': 'password',
                'class': 'form-control',
                'placeholder': 'password',
                'required': 'required'
            })
        }


# class TestScopeForm(ModelForm):
#     class Meta:
#         model = TestData
#         fields = ["amplitude", "time"]
#         widgets = {
#             "amplitude": NumberInput(attrs={
#                 'type': 'range',
#                 'class': 'form-control-range',
#                 'id': 'amplitude',
#                 'min': '1',
#                 'max': '900',
#                 'oninput': 'changed_range()'
#             }),
#             "time": NumberInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Время',
#                 'step': '0.01',
#                 'min': '0.01',
#                 'max': '12'
#             })
#         }

class GeneratorForm(ModelForm):
    class Meta:
        model = SignalGenerator
        fields = ("channel", "sig_form", "frequency", "amplitude")
        # fields = ("frequency", "amplitude")


class ScopeForm(ModelForm):
    class Meta:
        model = Oscilloscope
        fields = ("ch_scale","time_base")
        # '''
        # widgets = {
        #     "ch_scale": TextInput,
        #     "time_base": TextInput,
        # }
        # '''