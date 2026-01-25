from . import views
from django.urls import path, include

urlpatterns = [
    path("/student",views.student_registration,name='student_registration')
]
