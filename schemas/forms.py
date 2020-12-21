from django import forms


class DataSetForm(forms.Form):
    rows = forms.IntegerField()
