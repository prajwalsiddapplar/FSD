from django import forms

class BiodataForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
