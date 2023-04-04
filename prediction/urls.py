from django.urls import path
from . import views
urlpatterns=[path("/",views.fun,name="f"),
path("/externals",views.prediction,name="c"),
]