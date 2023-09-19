from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path("student.html",views.student, name='student'),
    path("wardendashboard.html", views.wardendashboard, name="wardendashboard")
]