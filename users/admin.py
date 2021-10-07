from django.contrib import admin

from users.models import EmailUser, Contact

admin.site.register(EmailUser)
admin.site.register(Contact)