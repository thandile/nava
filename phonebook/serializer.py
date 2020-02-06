from rest_framework import serializers
from .models import PhonebookEntry


class PhonebookEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonebookEntry
        fields = ('id', 'name', 'surname', 'country_code', 'number', 'country')
