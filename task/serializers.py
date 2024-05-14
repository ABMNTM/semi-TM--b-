from rest_framework.serializers import Serializer , ModelSerializer
from .models import List , Task , Comment
from usualFuncs import generator





# class TaskCreateSerializer(ModelSerializer):

#     class Meta:
#         model = Task
#         fields = ()







# class TaskCLSerializer(ModelSerializer):

#     class Meta:
#         model = Task
#         fields = '__all__'
#         extra_kwargs = {
#             'percentage'   : generator(read_only = True),
#             'id'           : generator(read_only = True),
#             'date_created' : generator(read_only = True),
#         }

# class TaskSerializerInner(ModelSerializer):

#     class Meta:
#         model = Task
#         excludes = ('list',)
#         extra_kwargs = {
#             'id'           : generator(read_only = True),
#             'date_created' : generator(read_only = True),
#         }


# class ListCLSerializer(ModelSerializer):

#     tasks = TaskSerializerInner(many = True, source = 'tasks', required = False, read_only = True)
    
#     class Meta:
#         model = List
#         fields = ('id' , 'name' , 'project' , 'date_created' , 'tasks')
#         extra_kwargs = {
#             'id'           : generator(read_only  = True),
#             'date_created' : generator(read_only  = True),
#             'project'      : generator(write_only = True),
#         }

# class ListUDSerializer(ModelSerializer):

#     class Meta:
#         model = List
#         excludes = ('project',)
#         extra_kwargs = {
#             'date_created' : generator(read_only = True),
#         }


    
