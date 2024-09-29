# gpf/forms.py

from django import forms
from .models import GPFForm, Nominee

class GPFFormForm(forms.ModelForm):
    class Meta:
        model = GPFForm
        fields = ['name', 'permanent_address', 'phone_number', 'marital_status']

class NomineeForm(forms.ModelForm):
    class Meta:
        model = Nominee
        fields = ['name', 'relationship', 'age', 'share_percentage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'share_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }
