from django import forms


class ProductoFormulario(forms.Form):

    nombre = forms.CharField()
    serie = forms.IntegerField()
