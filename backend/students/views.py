from django.shortcuts import render
from assignments.models import Assignment

def student_available_assignments(request,student_id):
      
    available_assigments=Assignment.objects.all()

    return render(request,'student_available_assignments.html',{'assignments':available_assigments,'student_id':student_id}) 

def assignment_submission(request,student_id,assignment_id):

    return render(request,'assignment_submission_page.html')