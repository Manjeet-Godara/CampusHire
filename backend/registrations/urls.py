from . import views
from django.urls import path, include

urlpatterns = [
    path("student",views.student_registration,name='student_registration'),
    path('company', views.company_registration,name='company_registration'),
    path('thanks',views.thanks,name='thanks')
]
