from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pickle
import json
import numpy as np
def fun(request):
	template=loader.get_template("f1.html")
	return HttpResponse(template.render())
def prediction(request):
    t=request.GET
    s=int(t.get("sqft"))
    bh=int(t.get("bhk"))
    ba=int(t.get("bath"))
    loc=t.get("location")
    with open("C:/Users/chera/pred_model.txt","rb") as f:
        model=pickle.load(f)
    f.close()
    with open("C:/Users/chera/columns.json") as f:
        data=json.load(f)
    f.close()
    columns=data["data_columns"][3:]
    a=np.zeros(len(columns)+3)
    a[0]=ba
    a[1]=bh
    a[2]=s
    a[3+columns.index(loc)]=1
    return render(request,"f1.html",{"data":model.predict([a])[0]})
# Create your views here.
