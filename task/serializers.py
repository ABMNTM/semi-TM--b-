from rest_framework import serializers as srzs
from .models import List , Task , Comment
from usualFuncs import generator


class TaskCreateSerializer(srzs.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'context', 'status', 'related_list')
        extra_kwargs = {
            'id' : generator(read_only = True),
        }

class TaskURDSerializer(srzs.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'id' : generator(read_only = True),
        }

class TaskListSerializer(srzs.ModelSerializer):

    comment_count = srzs.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'context', 'status', 'comment_count')
        extra_kwargs = {
            'id' : generator(read_only = True),
        }

    def get_comment_count(self, obj):
        return obj.comments.count()

class ListLSerializer(srzs.ModelSerializer):

    tasks = TaskListSerializer(many = True )
    
    class Meta:
        model = List
        fields = ('id' , 'name', 'tasks')
        extra_kwargs = {
            'id'           : generator(read_only  = True),
            'date_created' : generator(read_only  = True),
        }

class ListCreateSerializer(srzs.ModelSerializer):
    
    class Meta:
        model = List
        fields = ('id', 'name', 'project')
        extra_kwargs = {
            'id' : generator(read_only = True),
        }

class ListUDSerializer(srzs.ModelSerializer):

    class Meta:
        model = List
        exclude = ('project',)
        extra_kwargs = {
            'date_created' : generator(read_only = True),
        }
