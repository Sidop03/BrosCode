from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='hostelportal'),
    path('csvwarden',views.csvwarden, name='csvwarden'),
    path('csvstudent',views.csvstudent, name='csvstudent'),
    path("page",views.page,name='page')
]
