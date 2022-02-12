from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="home" ),
    path("shop",views.temp, name ="temp"),
    path("about",views.about, name ="about"),
    path("contact",views.contact, name ="contact"),
    path("prodview",views.view, name ="prodview"),
    path("checkout",views.out, name ="out"),
]
