from django.urls import path
from rest_framework import routers

from . import views
from .views import ContactsCreateApi, ContactsUpdateApi, ContactsDeleteApi, ContactsViewApi

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactsViewSet)

urlpatterns = [
    path('create/', ContactsCreateApi.as_view()),
    path('update/<int:pk>/', ContactsUpdateApi.as_view()),
    path('show/<int:pk>/', ContactsViewApi.as_view()),
    path('delete/<int:pk>/', ContactsDeleteApi.as_view()),
]
