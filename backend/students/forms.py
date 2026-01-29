from django import forms 
from assignments.models import AssignmentsSubmitted

class Student_Assignment_Submission(forms.ModelForm):
    class Meta:
        model=AssignmentsSubmitted
        fields={'uploaded_file'}
        #widgets={'submitted_at':forms.HiddenInput,'is_late':forms.HiddenInput,'similarity':forms.HiddenInput,'redflagged':forms.HiddenInput}