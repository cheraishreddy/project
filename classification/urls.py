from . import views
from . import l
from django.urls import path
urlpatterns=[path("/1",l.a,name="l"),path("/",views.fun,name="fun"),]