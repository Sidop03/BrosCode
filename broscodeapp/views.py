from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'hostelportal.html')
def student(request):
    name = request.GET["name"]
    regNo = request.GET["regNo"]
    CurrBlock = request.GET["cblock"]
    ReqBlock = request.GET["rblock"]
    roomtype = request.GET["room-type"]
    bedtype = request.GET["bed-type"]

    return render(request,'student.html')
def wardendashboard(request):
    return render(request, 'wardendashboard.html')

    wardenname = request.GET["wname"]
    empid = request.GET["empId"]
    block = request.GET["block"]
    roomtype = request.GET["room-type"]
    bedtype = request.GET["bed-type"]
    