from django.urls import path
from django.conf.urls import handler404
from . import views
from .views import subscribe, messages_form, admin_dashboard
from .views import admin_login, admin_logout


urlpatterns = [
    path("", views.home, name="home_in"),
    path("home/", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("subscribe/", subscribe, name="subscribe"),
    path("messages_form/", messages_form, name="messages_form"),
    # path("admin/signup/", views.admin_signup, name="admin_signup"),
    path("admin/login/", admin_login, name="admin_login"),
    path("admin/logout/", admin_logout, name="admin_logout"),
    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
]
