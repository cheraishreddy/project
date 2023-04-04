from django.urls import path
from . import views
urlpatterns=[path('p/',views.index,name='index1'),
path('b/',views.i,name='l')]