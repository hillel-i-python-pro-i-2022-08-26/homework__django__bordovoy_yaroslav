from django.urls import path

from . import views

app_name = "contacts_db"

urlpatterns = [
    path("", views.ContactsListView.as_view(), name="index"),
    path("create-contact/", views.ContactsCreateView.as_view(), name="create_contact"),
    path("search-contact/", views.search_contact, name="search_contact"),
    path("read-contact/", views.read_contact, name="read_contact"),
    path(
        "delete-contact/<int:pk>/",
        views.ContactsDeleteView.as_view(),
        name="delete_contact",
    ),
    path(
        "update-contact/<int:pk>/",
        views.ContactsUpdateView.as_view(),
        name="update_contact",
    ),
    # path("contact/<int:pk>/", views.ContactsView.as_view(), name="contact"),
    path("contact/<int:pk>/", views.contact, name="contact"),
]
