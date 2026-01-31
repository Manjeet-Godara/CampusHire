from django.shortcuts import render
from assignments.models import Assignment
from .forms import Student_Assignment_Submission
from orgs.models import Student
from plagiarism_engine.preprocessing import get_string

def student_available_assignments(request,student_id):
      
    available_assigments=Assignment.objects.all()

    return render(request,'student_available_assignments.html',{'assignments':available_assigments,'student_id':student_id}) 

def assignment_submission(request,student_id,assignment_id):
    if request.method=='POST':
        form = Student_Assignment_Submission(request.POST,request.FILES)
        if form.is_valid():
            
            submission=form.save(commit=False)
            submission.student=Student.objects.get(id=student_id)
            submission.assignment=Assignment.objects.get(id=assignment_id)
            submission.is_late=False
            submission.similarity=100
            submission.similarity_with=Student.objects.get(id=student_id)
            submission.redflagged=False

            uploaded_file=request.FILES['uploaded_file']
            
            print(get_string(uploaded_file))

            #submission.save()
            return render(request,'success.html')
    else:
        form=Student_Assignment_Submission()
    return render(request,'assignment_submission_page.html',{'form':form,'student_id':student_id,'assignment_id':assignment_id})

