# Generated by Django 3.2.7 on 2021-09-15 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='replies', to='mails.mail'),
        ),
    ]