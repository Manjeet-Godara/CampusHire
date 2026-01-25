from django.shortcuts import render, redirect
from .forms import Student_Registration


def student_registration(request):
    
    if request.method=="POST":
        form=Student_Registration(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('thanks')
        else:
            print("Enter valid data")
    else:       
        form=Student_Registration()

    return render(request,'student_registration.html',{'form':form}) 

def thanks(request):
    return render(request,'thanks.html')
    
