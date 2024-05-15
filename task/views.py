from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import serializers
from rest_framework import generics, views
from .models import List , Task , Comment
from rest_framework import status

class ListCreateList(views.APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        try:
            assert(request.GET.get('project') is not None)
            Lists = List.objects.filter(project = request.GET.get('project')).all()
            srz = serializers.ListLSerializer(instance = Lists, many = True)
            return Response(data = srz.data)
        except AssertionError as e:
            data = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'details': 'مقدار project نمی تواند خالی باشد'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        srz = serializers.ListCreateSerializer(data = request.data)
        srz.is_valid(raise_exception = True)
        srz.save()
        return Response(status = status.HTTP_201_CREATED)
    

class ListUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return List.objects.filter(project__board__owner = self.request.user)
    
    serializer_class = serializers.ListUDSerializer

class TaskCreate(generics.CreateAPIView):

    permission_classes = (IsAuthenticated,)

    queryset = Task

    serializer_class = serializers.TaskCreateSerializer


class TaskURD(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(related_list__project__board__owner = self.request.user)
    
    serializer_class = serializers.TaskURDSerializer