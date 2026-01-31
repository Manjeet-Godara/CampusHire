from django.shortcuts import render
from assignments.models import Assignment, AssignmentsSubmitted
from .forms import Student_Assignment_Submission
from orgs.models import Student
from plagiarism_engine.preprocessing import get_string
from plagiarism_engine.algorithms import create_n_grams, jaccards_similarity
from django.utils import timezone

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

            uploaded_file=request.FILES['uploaded_file2']
            created_chunks=create_n_grams(get_string(uploaded_file),4)
            submission.chunks= created_chunks
            
            other_assignments=AssignmentsSubmitted.objects.filter(assignment=submission.assignment)
            
            max_similarity=0
            max_similarity_with=None 
            for i in other_assignments:
                if i.student==submission.student:
                    pass
                
                similarity=jaccards_similarity(created_chunks,i.chunks)

                if similarity>max_similarity:
                    max_similarity=similarity
                    max_similarity_with=i.student
            
            if max_similarity_with==None:
                submission.similarity_with=Student.objects.get(id=student_id)
                submission.similarity=0
            else:
                submission.similarity_with=max_similarity_with
                submission.similarity=max_similarity
            
            if max_similarity>=50:
                submission.redflagged=True
            
            if timezone.now()>submission.assignment.deadline:
                submission.is_late=True
                
            submission.save()
            return render(request,'success.html')
    else:
        form=Student_Assignment_Submission()
    return render(request,'assignment_submission_page.html',{'form':form,'student_id':student_id,'assignment_id':assignment_id})

