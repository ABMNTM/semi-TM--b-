from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import serializers
from rest_framework import generics
from .models import List , Task , Comment


# class ListCLView(generics.ListCreateAPIView):

#     permission_classes = (IsAuthenticated,)
#     serializer_class = serializers.ListCLSerializer

#     def get_queryset(self):
#         return List.objects.select_related().filter(project = serializer_class.data['project'])
    

# # do not need to retreve any list
# class ListUDView(generics.UpdateAPIView , generics.DestroyAPIView):

#     permission_classes = (IsAuthenticated,)
#     serializer_class = serializers.ListURDSerializer

#     def get_queryset(self):
#         return List.objects.select_related().filter(project__board__owner = self.request.user)



# # we don't need listing the task (listing will done in listView)
# class TaskCView(generics.CreateAPIView):

#     permission_classes = (IsAuthenticated,)
#     serializer_class = serializers.TaskCLSerializer

#     def get_queryset(self):
#         return Task.objects.select_related().filter(project__board__owner = self.request.user)

# # don't need to retrieve ...
# class TaskUDView(generics.RetrieveUpdateDestroyAPIView):

#     permission_classes = (IsAuthenticated,)
#     serializer_class = serializers.TaskCLSerializer

#     def get_queryset(self):
#         return Task.objects.select_related().filter(project__board__owner = self.request.user)
