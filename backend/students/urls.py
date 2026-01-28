from django.urls import path
from . import views

urlpatterns = [
    path('available_assignments',views.student_available_assignments,name='student_available_assignments'),
    path('assignment/<int:id>/',views.assignment_submission,name='assignment_submission')
]
