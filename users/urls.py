from django.urls import path
from . import views


urlpatterns = [
    path('create-user', views.create_user),
    path('change-password', views.ChangePassword.as_view()),
    path('get-contacts', views.GetContacts.as_view()),
    path('get', views.get)
]