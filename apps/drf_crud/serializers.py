from rest_framework import serializers

from apps.contacts_db.models import Contacts


class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
