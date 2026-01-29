from django.db import models
from django.utils import timezone
from orgs.models import Company, Student
import os
import uuid

def unique_file_name(instance,filename):
    print(instance,",",filename)
    ext=filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads', filename)

class Assignment(models.Model):

    name=models.CharField(max_length=100, default='')
    company=models.ForeignKey(Company, on_delete=models.CASCADE,default='')
    published_at=models.DateTimeField(default=timezone.now)
    deadline=models.DateTimeField(default=timezone.now)
    role=models.CharField(max_length=100, default='')
    description=models.CharField(max_length=400, default='')
    ctc=models.IntegerField(default=0)

class AssignmentsSubmitted(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default='',related_name='student')
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE,default='')
    submitted_at=models.DateTimeField(default=timezone.now)
    is_late=models.BooleanField(default=False)
    similarity=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    similarity_with=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='similarity_link')
    redflagged=models.BooleanField(default=False)
    uploaded_file=models.FileField(upload_to=unique_file_name) 


    



