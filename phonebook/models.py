from django.db import models


class PhonebookEntry(models.Model):
    name = models.CharField(max_length=245)
    surname = models.CharField(max_length=245)
    country_code = models.BigIntegerField()
    number = models.BigIntegerField()
    country = models.CharField(max_length=245)
