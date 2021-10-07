from django.db.models import QuerySet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from .models import EmailUser, Contact
from .serializers import EmailUserSerializer, ChangePasswordSerializer


@api_view(['POST'])
@permission_classes([AllowAny, ])
def create_user(request):
    serializer = EmailUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePassword(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                token, created = Token.objects.get_or_create(user=user)
                token.delete()
                token.created = Token.objects.create(user=user)
                return Response({"message": "password changed successfully"}, status=status.HTTP_200_OK)
            return Response({"message": "old_password is wrong"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetContacts(generics.ListAPIView):
    def get_queryset(self):
        return self.request.user.contacts

    def get_serializer_class(self):
        return EmailUserSerializer


@api_view(['POST', ])
def add_contact(request, pk):
    try:
        user = EmailUser.objects.get(pk=pk)
    except:
        return Response({"message": "user with this id doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
    contact = Contact.objects.create(owner=request.user, contact=user)
    contact.save()
    return Response({"message": "contact added successfully"}, status=status.HTTP_200_OK)


class GetContacts(generics.ListAPIView):
    def get_queryset(self):
        return EmailUser.objects.filter(contact__owner=self.request.user)

    serializer_class = EmailUserSerializer
