from django.db import models
from instructor.models import Instructor
from students.models import Student
from blocks.models import Block
# Create your models here.
class SchoolForm(models.Model):
	form_name=models.CharField(max_length=60, default="School Form 1")
	block=models.ForeignKey(Block, on_delete=models.CASCADE)
	instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE)
	student=models.ForeignKey(Student, on_delete=models.CASCADE)
	def sf_name(self):
		sfname="%s - %s (%s)"%(self.form_name, self.instructor, self.block)
		return sfname

	def __str__(self):
		return self.sf_name()