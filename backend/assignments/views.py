from django.shortcuts import render, redirect
from .forms import Assignment_creation_Form

def create_assignment(request):
    if request.method=='POST':
        form=Assignment_creation_Form(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            print('Enter valid data')
    else:
        form=Assignment_creation_Form()
    return render(request,'assignment_creation.html',{'form':form})



