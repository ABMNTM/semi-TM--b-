from django.contrib.auth.models import User
from rest_framework import generics , status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from .permissions import IsAuthenticatedAndOwner
from . import serializers


class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects
    serializer_class = serializers.UserCreateSerializer

    def create(self, request, *args, **kwargs):
        srz = self.serializer_class(data=request.data)
        if srz.is_valid():
            passwd = srz.validated_data.pop('password')
            user = User.objects.create_user(**srz.validated_data)
            user.set_password(passwd)
            user.save()
            headers = self.get_success_headers(srz.data)
            return Response(srz.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST)

    
class UserURDView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserRUDSerializer
        
    def get_object(self , queryset = None):
        return self.request.user

    
class UserPasswordUpdateView(generics.UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    model = User
    serializer_class = serializers.UserPasswordUpdateSerializer

    def get_object(self , queryset = None):
        obj = self.request.user
        return obj

    def update(self , request , *arrgs , **kwargs):
        self.object = self.get_object()
        srz = self.serializer_class(data = request.data)

        if srz.is_valid():
            # password check
            if not self.object.check_password(srz.validated_data['old_password']):
                return Response(
                    status = status.HTTP_400_BAD_REQUEST,
                    data = {'error' : 'password doesn\'t match.'},
                )
            # new password saving ...
            self.object.set_password(srz.validated_data['new_password'])
            self.object.save()
            response = {
                'status' : 'success',
                'code'   :  status.HTTP_200_OK,
                'message': 'password updated successfully',
                'data'   :  [],
            }
            return Response(response , status = status.HTTP_200_OK)
        return Response(srz.errors , status = status.HTTP_400_BAD_REQUEST)