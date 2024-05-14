from django.contrib.auth.models import User
from rest_framework import serializers
from . import models
from usualFuncs import generator

class ProjectSerializerInner(serializers.ModelSerializer):

	class Meta:
		model = models.Project
		fields = ( 'id' , 'name', 'isStared')
		extra_kwargs = {
			'id'         : generator(read_only = True),
			'created_at' : generator(read_only = True),
		}
	
class BoardSerializer(serializers.ModelSerializer):

	projects = ProjectSerializerInner(many = True, source = 'project_set', required = False)

	class Meta:
		model = models.Board
		fields = ('id' , 'name', 'isArcheved', 'projects')
		extra_kwargs = {
			'id' : generator(read_only = True ),
		}

class ProjectSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Project
		fields = ('id' , 'name' , 'board')
		extra_kwargs = {
			'id' : generator(read_only = True ),
		}