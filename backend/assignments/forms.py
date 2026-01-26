from django import forms
from assignments.models import Assignment, AssignmentsSubmitted

class Assignment_creation_Form(forms.ModelForm):
    class Meta:
        model=Assignment
        fields={'name','company','published_at','deadline','role','description','ctc'}
        widgets={
            'published_at':forms.HiddenInput()
        }
    
# class Assignment_Submission_Form(forms.ModelForm):
#     class Meta:
#         model= AssignmentsSubmitted
#         fields={'student','assignment','submitted_at','is_late','similarity','similarity_with','redflagged','uploaded_file'}
#         widgets={
#             'assigne'
#         }

