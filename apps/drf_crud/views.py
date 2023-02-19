from rest_framework import viewsets, permissions, generics

from apps.contacts_db.models import Contacts
from apps.drf_crud.serializers import ContactsSerializer


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactsViewApi(generics.RetrieveAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactsCreateApi(generics.CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactsUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactsDeleteApi(generics.RetrieveDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]
