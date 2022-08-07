from re import T
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from predicts.models import Predicts

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def about(response):
    return render(response, "main/about.html", {})

def usstockpick(response):
    plist = Predicts.objects.all()
    for item in plist:
        print(item.__str__())
    return render(response, "main/usstockpick.html", {'plist':plist})