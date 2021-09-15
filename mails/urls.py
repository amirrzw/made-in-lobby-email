from django.urls import path
from . import views


urlpatterns = [
    path('get-post-mail', views.CreateAndGetPosts.as_view()),
    path('get-sent-mails', views.get_sent_mails),
    path('get-replies/<int:pk>', views.get_replies),
    path('mail-detail/<int:pk>', views.MailDetail.as_view()),
    path('delete-mail/<int:pk>', views.DeleteMail.as_view()),
]