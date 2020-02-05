from django.db import models


class PhonebookEntry(models.Model):
    name = models.CharField(max_length=245)
    surname = models.CharField(max_length=245)
    number = models.CharField(max_length=245)
    address_line_1 = models.CharField(max_length=245)
    address_line_2 = models.CharField(max_length=245)
    address_line_3 = models.CharField(max_length=245)

