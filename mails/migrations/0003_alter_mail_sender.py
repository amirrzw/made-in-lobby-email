# Generated by Django 3.2.7 on 2021-09-15 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mails', '0002_mail_reply_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_mails', to=settings.AUTH_USER_MODEL),
        ),
    ]
