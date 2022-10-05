from django.urls import path
from . import views

urlpatterns = [
    path("", views.greeting_for_user, name="index"),
    path("<str:username>", views.greeting_for_user, name="index"),
]
