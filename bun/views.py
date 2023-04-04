from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import M
def index(request):
    t=loader.get_template("a.html")
    return HttpResponse(t.render())
def i1(req):
	o=M.objects.all().values()
	return HttpResponse(o[0]["first"])
# Create your views here.
