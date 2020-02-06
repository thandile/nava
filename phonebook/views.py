from rest_framework import viewsets
from .models import PhonebookEntry
from .serializer import PhonebookEntrySerializer


class PhonebookEntryView(viewsets.ModelViewSet):
    queryset = PhonebookEntry.objects.all()
    serializer_class = PhonebookEntrySerializer