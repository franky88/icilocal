from django.db import models

# Create your models here.
class Block(models.Model):
	block_name=models.CharField(max_length=60, unique=True)
	date_add=models.DateField(auto_now=False, auto_now_add=True)
	date_updated=models.DateField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.block_name