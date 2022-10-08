from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path("", views.greeting_for_user, name="index"),
    path("<str:username>", views.greeting_for_user, name="index"),
]
