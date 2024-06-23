from django import forms
from django.forms import TextInput, EmailInput, Select, Textarea

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback

        fields = ['first_name','last_name','email','trainer','message']

        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter you first name...'}),
            'last_name' : TextInput(attrs={'class':'form-control', 'placeholder':'Please enter you last name...'}),
            'email': EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your e-mail'}),
            'trainer': Select(attrs={'class':'form-control'}),
            'message': Textarea(attrs={'class':'form-control','placeholder':'Please write your feedback', 'rows':'3'}),

        }

