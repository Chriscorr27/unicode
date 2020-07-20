from django import forms

class InputForm(forms.Form):
    starting = forms.IntegerField()
    ending = forms.IntegerField()