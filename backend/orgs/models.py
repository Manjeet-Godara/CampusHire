from django.db import models
from django.utils import timezone

class Company(models.Model):
    name=models.CharField(max_length=100)
    representative_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10,default='')
    email=models.EmailField(max_length=254,default='')
    address=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

class Student(models.Model):

    name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=100)
    gender=models.CharField(default='',choices=[('Male','Male'),('Female','Female')])
    age=models.IntegerField()
    address=models.CharField(max_length=100,default='')
    cgpa=models.DecimalField(max_digits=4,decimal_places=2)
    phone=models.CharField(max_length=10,default='')
    email=models.EmailField(max_length=254,default='')
    skills=models.CharField(choices=[('Web Development','Web Development'),('AI and Data Science','AI and Data Science'),('Game Development','Game Development')],default='')
    placed=models.BooleanField(default=False)
    company_placed_in=models.ForeignKey(Company, on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.name
    
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
    is_late=models.BooleanField(default='')
    similarity=models.DecimalField(max_digits=5,decimal_places=2)
    similarity_with=models.ForeignKey(Student,on_delete=models.CASCADE,default='',related_name='similarity_link')
    redflagged=models.BooleanField(default='')
    #uploaded_file=models.FileField()


    


