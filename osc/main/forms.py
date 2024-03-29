from .models import Oscilloscope, SignalGenerator
from django.forms import ModelForm, TextInput, PasswordInput
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

class GeneratorForm(ModelForm):
    class Meta:
        model = SignalGenerator
        fields = ("channel", "sig_form", "frequency", "amplitude")


class ScopeForm(ModelForm):
    class Meta:
        model = Oscilloscope
        fields = ("ch_scale","time_base")