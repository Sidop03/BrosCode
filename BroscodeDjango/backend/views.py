from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import os
from datetime import datetime
url= "https://raw.githubusercontent.com/Sidop03/BrosCode/main/oursheet%20-%20Sheet1.csv"
df = pd.read_csv(url)
print(df['Name'])
# Create your views here.
def home(request):
    return render(request,'hostelportal.html',{'NAME':'HARSHIT'})
def csvwarden(request):
    return render(request, "wardendashboard.html")
def csvstudent(request):
    return render(request, "student.html")
def page(request):
    wname = request.GET['wname']
    empId = request.GET['empId']
    wblock = request.GET['block']
    wnamelist = []          
    empIdlist = []         
    wblocklist = []
    print(wname, "this is wname")    
    print(empId, "this is empId")    
    for i in range(len(df['Warden Name'])):
        wnamelist.append(df['Warden Name'][i])
        empIdlist.append(df['Employee ID'][i])
        wblocklist.append(df['Warden\'s Block'][i])

    # Assuming you have empId, wname, and wblock as variables

    finallist = []

    # You need to use a loop to iterate over the existing DataFrame, not just based on the length of empIdlist
    for i in range(len(df['Warden Name'])):
        finallist.append([wnamelist[i], empIdlist[i], wblocklist[i]])
    if empId not in empIdlist:
        wnamelist.append(wname)
        empIdlist.append(empId)
        wblocklist.append(wblock)
        finallist.append([wnamelist[-1], empIdlist[-1], wblocklist[-1]])
    print(wblocklist)
    print(finallist)
    dfe = pd.DataFrame(finallist)
    print(dfe,"this isdatafram")
    dfe.to_csv('oursheet - Sheet1.csv')
    # os.system("git add r'BroscodeDjango/backend/oursheet - Sheet1.csv'")
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # os.system("git commit -m 'changed again{dt_string}'")
    # os.system("git push origin master")
    return render(request,'page.html')