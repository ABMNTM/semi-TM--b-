from django.contrib.auth.models import User
from rest_framework import generics , mixins , permissions , authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status , serializers as srzs
from . import serializers , models


class BoardCLView(generics.ListCreateAPIView):

	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		return models.Board.objects.filter(owner = self.request.user)
	
	serializer_class = serializers.BoardSerializer

	def create(self, request, *args, **kwargs):
		srz_data = self.serializer_class(data = request.data)
		if srz_data.is_valid():
			srz_data.validated_data['owner'] = request.user
			srz_data.save()
			return Response(data = srz_data.data, status = status.HTTP_201_CREATED)
		return Response(data = srz_data.errors, status = status.HTTP_400_BAD_REQUEST)

class BoardURDView(generics.RetrieveUpdateDestroyAPIView):

	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		return models.Board.objects.filter(owner = self.request.user)
	
	serializer_class = serializers.BoardSerializer

class ProjectCLView(generics.ListCreateAPIView):

	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		return models.Project.objects.select_related().filter(board__owner = self.request.user)

	serializer_class = serializers.ProjectSerializer

class ProjectURDView(generics.RetrieveUpdateDestroyAPIView):

	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		return models.Project.objects.select_related().filter(board__owner = self.request.user)

	serializer_class = serializers.ProjectSerializer