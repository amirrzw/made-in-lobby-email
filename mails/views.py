from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from mails.models import Mail
from mails.serializers import MailReadSerializer, MailSerializer
from .permissions import IsAuthor


class CreateAndGetPosts(generics.ListCreateAPIView):
    def get_queryset(self):
        return Mail.objects.filter(receiver=self.request.user)
        # return self.request.user.inbox

    def get_serializer_class(self):
        if self.request in permissions.SAFE_METHODS:
            return MailReadSerializer
        else:
            return MailSerializer


@api_view(['GET', ])
def get_sent_mails(request):
    # mails = request.user.mail_set
    mails = Mail.objects.filter(sender=request.user)
    serializer = MailReadSerializer(mails, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class MailDetail(generics.RetrieveAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailReadSerializer
    permission_classes = (IsAuthor, )

class DeleteMail(generics.DestroyAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailReadSerializer
    permission_classes = (IsAuthor,)


@api_view(['GET'], )
@permission_classes([IsAuthor, ])
def get_replies(request, pk):
    try:
        replies = Mail.objects.get(pk=pk).replies
    except:
        return Response({"message": "mail with this id doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = MailReadSerializer(replies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


