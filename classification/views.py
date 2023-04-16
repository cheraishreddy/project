from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
import pickle
face=cv2.CascadeClassifier("staticfiles/haar-cascade-files-master/haar-cascade-files-master/haarcascade_frontalface_default.xml")
eye=cv2.CascadeClassifier("staticfiles/haar-cascade-files-master/haar-cascade-files-master/haarcascade_eye.xml")
def load(request):
	t=loader.get_template("load.html")
	return HttpResponse(t.render())
@csrf_exempt
def fun(request): 
	if(request.method=="GET"):
		t=loader.get_template("load.html")
		return render(request,"load.html")
	req=request.POST
	img=""
	try:
		img=request.FILES['file']
	except:
		return render(request,"load.html",{"data":0})
	fs=FileSystemStorage()
	fs.save(img.name,img)
	url="classification/static/media"+"/"+str(img.name) 
	img=fun1(url)
	try:
		if(img==None):
			os.remove(url)
			return render(request,"load.html",{"data":0})
	except:
		pass
	with open("classify.txt","rb") as f:
		model=pickle.load(f)
	img=cv2.resize(img,(64,64))
	t=np.array([img])
	data=np.argmax(model.predict(t))
	os.remove(url)
	return render(request,"load.html",{"data":data+1})
def fun1(url):
    img=cv2.imread(url)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f=face.detectMultiScale(gray)
    for (x,y,w,h) in f:
        rg=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye.detectMultiScale(rg)
        if len(eyes)>=2:
            return roi_color

