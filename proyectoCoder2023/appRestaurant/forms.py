from django import forms

class formCategoria(forms.Form):
    campNombre= forms.CharField()
    campDescrip = forms.CharField()
    campActivo = forms.CharField()
    