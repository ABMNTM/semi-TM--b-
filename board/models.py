from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):

	name = models.CharField(max_length=250)
	date_created = models.DateTimeField(auto_now = True)
	isArcheved = models.BooleanField(default = False)
	owner = models.ForeignKey(User , on_delete = models.CASCADE, related_name = 'Board_set')

	def __str__(self):
		return self.name
		

class Project(models.Model):

	name = models.CharField(max_length = 250)
	created_at = models.DateTimeField(auto_now = True)
	isStared = models.BooleanField(default = False)
	board = models.ForeignKey(Board, on_delete = models.CASCADE , related_name = 'project_set')

	def __str__(self):
		return f'{self.board.name} - {self.name}'
