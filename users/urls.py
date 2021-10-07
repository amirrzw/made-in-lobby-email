from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('create-user', views.create_user),
    path('change-password', views.ChangePassword.as_view()),
    path('get-contacts', views.GetContacts.as_view()),
    path('get-token', obtain_auth_token),
    path('add-contact/<int:pk>', views.add_contact),
    path('get-contacts', views.GetContacts.as_view()),
]