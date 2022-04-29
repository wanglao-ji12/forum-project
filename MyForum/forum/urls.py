from django.urls import URLPattern, path
from . import views

URLPattern=[
    path("",views.entry),
    path("index",views.index,name="index"),
    path("showposting",views.showPosting,name="showposting"),
    path("like",views.like,name="like"),
    path("collect",views.collect,name="collect"),
    path("comment",views.addComment,name="comment")
]