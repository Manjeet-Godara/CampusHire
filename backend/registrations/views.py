from django.shortcuts import render, redirect
from .forms import Student_Registration_Form, Company_Registration_Form


def student_registration(request):
    
    if request.method=="POST":
        form=Student_Registration_Form(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('thanks')
        else:
            print("Enter valid data")
    else:       
        form=Student_Registration_Form()

    return render(request,'student_registration.html',{'form':form}) 

def company_registration(request):
    print('me')
    if request.method=='POST':
        form=Company_Registration_Form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            print("Enter valid data")
    else:
        form=Company_Registration_Form()
    return render(request,'company_registration.html',{'form':form})

def thanks(request):
    return render(request,'thanks.html')
    
