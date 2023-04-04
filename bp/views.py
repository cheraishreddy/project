from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def index(request):
    t=loader.get_template("a.html")
    return HttpResponse(t.render())

# Create your views here.
def i(request):
    b=loader.get_template('a.html')
    return HttpResponse(b.render())
