from django.urls import URLPattern, path
from . import views

URLPattern=[
    path("",views.entry),
    path("index",views.index,name="index"),
    path("showposting",views.showPosting,name="showposting"),
    path("like",views.like,name="like"),
    path("co")
]