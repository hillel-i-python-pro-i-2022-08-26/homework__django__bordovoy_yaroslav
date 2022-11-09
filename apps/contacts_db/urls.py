from django.urls import path

from . import views

app_name = "contacts_db"

urlpatterns = [
    path("", views.show_all, name="index"),
    path("create-user/", views.create_contact, name="create_contact"),
    path("search-contact/", views.search_contact, name="search_contact"),
    path("read-contact/", views.read_contact, name="read_contact"),
    path("delete-contact/<int:pk>/", views.delete_contact, name="delete_contact"),
    path("update-contact/<int:pk>/", views.update_contact, name="update_contact"),
    path("contact/<int:pk>/", views.contact, name="contact"),
]
