from django import forms

from django.forms import Select, EmailInput, TextInput

from student.models import Student
from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course', 'email', 'department', 'active', 'profile']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your course'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'department': Select(attrs={'class': 'form-select'}),
        }

    def clean(self):

        clean_data = self.cleaned_data

        # Email Unique

        get_email = clean_data.get('email')

        check_email = Student.objects.filter(email=get_email)
        if check_email:
            msg = 'Exista adresa de email in sistem'
            self._errors['email'] = self.error_class([msg])

        return self.cleaned_data


class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course', 'email', 'department', 'active', 'profile']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your course'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'department': Select(attrs={'class': 'form-select'}),
        }
