from django.urls import path
from . import views
# from .views import validate_email



urlpatterns = [
    path("", views.home, name="home_in"),
    path("home/", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    # path("validate_email", validate_email, name="validate_email"),
]
