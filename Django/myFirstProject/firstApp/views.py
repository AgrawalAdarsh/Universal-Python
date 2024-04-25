from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def display(request):
    s="<h1>Hello Everyone This is Adarsh This side!</h1>"
    return HttpResponse(s)
def helloworld(request):
    s1="<h1>Hello World!!!</h1>"
    return HttpResponse(s1)
def oldtimer(request):
    mauth = datetime.now().strftime("%Y-%m-%d %h:%M:%S")
    result = f"<h1>Hello There Oldtimers Your Remaining time is : {mauth}</h1>"
    return HttpResponse(result)
def Alooji(request):
    return render(request,"DeadPool.html")
def Login(request):
    return render(request,"login.html")    