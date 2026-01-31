from django import forms 
from assignments.models import AssignmentsSubmitted

class Student_Assignment_Submission(forms.ModelForm):
    class Meta:
        model=AssignmentsSubmitted
        fields={}