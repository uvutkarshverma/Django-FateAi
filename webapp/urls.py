from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.About, name="About"),
    path("contact/", views.Contact, name="Contact"),
    path("dashboard/", views.Admin, name="Admin"),

    
]