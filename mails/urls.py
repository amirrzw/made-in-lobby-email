from django.urls import path
from . import views


urlpatterns = [
    path('get-post-mail', views.CreateAndGetPosts.as_view()),
    path('get-sent-mails', views.get_sent_mails),
]