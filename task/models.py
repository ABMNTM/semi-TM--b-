from django.db import models
from board.models import Project
from django.contrib.auth.models import User


class List(models.Model):

	name = models.CharField(max_length = 250)
	project = models.ForeignKey(Project , on_delete = models.CASCADE , related_name = 'lists')
	date_created = models.DateTimeField(auto_now = True)

	def __str__(self):
		return f'{self.id} {self.project.name} - {self.name}'

class Task(models.Model):

	todo = 'TD'
	doing = 'DI'
	done = 'DN'

	TASK_CHOICES = [
		(todo , 'برای انجام'),
		(doing , 'در حال انجام'),
		(done , 'انجام شده'),
	]

	related_list = models.ForeignKey(List , on_delete = models.CASCADE, null = True, related_name = 'tasks')

	context = models.TextField()
	status = models.CharField(default=todo, max_length = 2 ,choices = TASK_CHOICES)
	percentage = models.PositiveSmallIntegerField(default = 0)

	date_created = models.DateField(auto_now = True)
	dead_line = models.DateTimeField(null = True)

	def __str__(self) -> str:
		return f'task ({self.id}) - list ({self.related_list.name})'


class Comment(models.Model):

	content = models.TextField()
	date_created = models.DateTimeField(auto_now = True)
	task = models.ForeignKey(Task , on_delete = models.CASCADE, related_name = 'comments')
	author = models.ForeignKey(User , on_delete = models.SET_NULL , null = True)

	def __str__(self) -> str:
		return f'comment ({self.id}) from task ({self.task.id})'