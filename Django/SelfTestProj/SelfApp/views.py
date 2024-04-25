from django.shortcuts import render
from SelfApp import views
# Create your views here.
def LoginPage(request):
    return render(request,"Login.html")