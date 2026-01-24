from django.contrib import admin
from .models import Student,Company, Assignment, AssignmentsSubmitted

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Assignment)
admin.site.register(AssignmentsSubmitted)