from django.urls import path
from . import views
from .views import subscribe, messages_form


urlpatterns = [
    path("", views.home, name="home_in"),
    path("home/", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("subscribe/", subscribe, name="subscribe"),
    path("messages_form/", messages_form, name="messages_form"),
]
