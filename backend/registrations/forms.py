from django import forms 
from orgs.models import Student, Company

class Student_Registration_Form(forms.ModelForm):
    class Meta:  
        model=Student
        fields={'name','roll_no','gender','age','address','cgpa','phone','email','skills','placed','company_placed_in'}

        widgets={
            'placed':forms.HiddenInput(),
            'company_placed_in':forms.HiddenInput()
        }

class Company_Registration_Form(forms.ModelForm):
    class Meta:
        model=Company
        fields={'name','representative_name','address','phone','email'}