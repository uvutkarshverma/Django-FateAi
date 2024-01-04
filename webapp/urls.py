from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.About, name="About"),
    path("contact/", views.Contact, name="Contact"),
    path("dashboard/", views.Admin, name="Admin"),
    path("addlisting/", views.Addlisting, name="Addlisting"),
    path("updatelisting/<id>/", views.Updatelisting, name="Updatelisting"),
    path("search/", views.Search, name="Search"),
    path("disclaimer/", views.Disclaimer, name="Disclaimer"),
    path("privacy-policy/", views.PrivacyPolicy, name="PrivacyPolicy"),

    
]