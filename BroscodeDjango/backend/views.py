from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'hostelportal.html',{'NAME':'HARSHIT'})
def csvwarden(request):
    return render(request, "wardendashboard.html")
def goback(request):
    return render(request,'hostelportal.html')
def page(request):
    return render(request,'page.html')