from tabla.models import *
from django import forms
from django.forms import Form, CharField, TextInput
from django.contrib.auth import authenticate

class LoginForm(Form):
    cedula = CharField(max_length=10, widget=TextInput(attrs=
                                                          {"class": "form-control",
                                                           "placeholder": "Cedula...",
                                                           "type": "text",
                                                           "autofocus": True}))
    password = CharField(max_length=30, widget=TextInput(attrs=
                                                          {"class": "form-control",
                                                           "type": "password",
                                                           "placeholder": "Password..."}))
class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        widgets={
            'elm_nombre':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombre del elemento...'
            }),
            'elm_fila':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ej: 1, 2, 3, 4...'
            }),
            'elm_simbolo':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ej: K, H, Fr, Hr...'
            }),
            'elm_densidad':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ej: 0,123...'
            }),
            'elm_electronegatividad':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ej: 0,12...'
            }),
            'elm_valencia':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ej: +1...'
            }),
            'elm_peso_atomico':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ej: 12,345...'
            }),
            'elm_numero_atomico':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ej: 2, 3, 4...'
            }),
            'elm_configuracion_electronica':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ej: [Ar] 4s1...'
            }),
            'elm_descripcion':forms.Textarea(attrs={
                'class':'form-control',
            }),
            'elm_estado':forms.Select(attrs={
                'class':'form-control'
            })
        }
        fields = '__all__'
