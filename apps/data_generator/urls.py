from django.urls import path
from . import views

app_name = "users_data"

urlpatterns = [
    path("", views.users_data_view, name="index"),
    path("<int:amount>", views.users_data_view, name="index"),
]
