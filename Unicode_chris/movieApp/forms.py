from django import forms

class MovieForm(forms.Form):
    movie = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Search for movies','class':'p-2 form-control mr-sm-2 ','width':'5000','heigth':'300'}))