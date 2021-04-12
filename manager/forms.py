from django import forms
from .models import Patient
class add_patient_form(forms.Form):
    first_name = forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'first_name',
                                        'class': 'form-control'}))
    last_name = forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'last name','class': 'form-control'}))
    

    DOB = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd','class': 'form-control'}))
    
    tested_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd','class': 'form-control'}))

    test_choices = Patient.TESTS

    test = forms.CharField(widget=forms.Select(choices=test_choices,attrs={'class': 'form-control'}))

    
    tel_no= forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Telephone Number','class': 'form-control'}))

    address = forms.CharField(max_length=200,
        widget=forms.Textarea(attrs={'placeholder': 'address','class': 'form-control'}))


    status = forms.CharField(max_length=20,
        widget=forms.Select(choices=Patient.STATUSES,attrs={'placeholder': 'Status','class': 'form-control'}))

