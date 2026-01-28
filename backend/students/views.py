from django.shortcuts import render
from assignments.models import Assignment

def student_available_assignments(request):
      
    available_assigments=Assignment.objects.all()

    return render(request,'student_available_assignments.html',{'assignments':available_assigments}) 

def assignment_submission(request,id):
    return render(request,'assignment_submission_page.html')