from django.contrib.auth.models import User
from django.db import models

class Mail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name='inbox', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    # image ...
