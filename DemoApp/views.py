from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    return render (request,"hello.html",{"today":all})
    

def hello (request):
    today=datetime.datetime.now().date()
    time=datetime.datetime.now().time()
    #all=today.str() time.str()
    #all=datetime.datetime.now().str()
    all=str(today) +" Time :"+ str(time)
    #return render (request,"hello.html",{"today":all})
    return render (request,"Cyrus Studio.html",{"today":all})

def showNumber(request,number):
    text="SHowing your number : %s" %number
    return HttpResponse(text)
