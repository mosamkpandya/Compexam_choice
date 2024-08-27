from django import forms
from django.core.exceptions import ValidationError
from .models import UserData

def validate_phone_number(value):
    if len(value) != 10 or not value.isdigit():
        raise ValidationError("Phone number must be exactly 10 digits.")

def validate_email_domain(value):
    if not (value.endswith('@ljku.edu.in') or value.endswith('@mail.ljku.edu.in')):
        raise ValidationError("Email must be from the domain 'ljku.edu.in' or 'mail.ljku.edu.in'.")

class UserDataForm(forms.ModelForm):
    contact_no = forms.CharField(validators=[validate_phone_number])
    email = forms.EmailField(validators=[validate_email_domain])

    class Meta:
        model = UserData
        fields = ['name', 'enrollment_no', 'branch', 'contact_no', 'email', 'choices']
