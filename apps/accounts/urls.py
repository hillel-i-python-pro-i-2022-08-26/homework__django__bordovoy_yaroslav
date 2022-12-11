from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("signup/", views.SingUpView.as_view(), name="signup"),
    path("update/<int:pk>/", views.UserUpdateView.as_view(), name="update"),
]
