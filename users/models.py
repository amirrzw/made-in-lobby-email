from django.contrib.auth.models import User
from django.db import models

class EmailUser(User):
    email_address = models.CharField(max_length=80, unique=True)
    contacts = models.ManyToManyField('self', blank=True, null=True)