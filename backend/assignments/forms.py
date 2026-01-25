from django import forms
from assignments.models import Assignment

class Assignment_creation_Form(forms.ModelForm):
    class Meta:
        model=Assignment
        fields={'name','company','published_at','deadline','role','description','ctc'}
        widgets={
            'published_at':forms.HiddenInput()
        }
    
