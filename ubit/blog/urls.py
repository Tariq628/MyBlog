from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("prodview/<int:myid>", views.prodview, name="prodView"),
    path("addpost/", views.addpost, name="addpost"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about")
]