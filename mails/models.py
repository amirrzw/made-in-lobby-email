from users.models import EmailUser
from django.db import models

class Mail(models.Model):
    sender = models.ForeignKey(EmailUser, related_name='sent_mails', on_delete=models.CASCADE)
    receiver = models.ForeignKey(EmailUser, related_name='inbox', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='replies')
    # image ...

    def __str__(self):
        return self.subject
