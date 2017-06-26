from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.
class Instructor(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	contact=models.CharField(max_length=13, blank=True)
	def __str__(self):
		return self.user.get_username()