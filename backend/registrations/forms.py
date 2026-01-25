from django import forms 
from orgs.models import Student

class Student_Registration(forms.ModelForm):
    class Meta:  
        model=Student
        fields={'name','roll_no','gender','age','address','cgpa','phone','email','skills','placed','company_placed_in'}

        widgets={
            'placed':forms.HiddenInput(),
            'company_placed_in':forms.HiddenInput()
        }