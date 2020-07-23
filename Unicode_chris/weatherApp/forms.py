from django import forms

class InputForm(forms.Form):
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter the City','class':'p-2 form-control mr-sm-2 ','width':'5000','heigth':'300'}))