from django.urls import path

from . import views

app_name = "contacts_db"

urlpatterns = [
    path("", views.contacts_view, name="index"),
]
