from django.urls import path
from . import views

urlpatterns = [
    path('available_assignments/<int:student_id>/',views.student_available_assignments,name='student_available_assignments'),
    path('assignment/<int:student_id>/<int:assignment_id>/',views.assignment_submission,name='assignment_submission')
]
