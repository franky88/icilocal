from django.db import models

# Create your models here.
class Gender(models.Model):
	gender=models.CharField(max_length=6, default="male")
	def __str__(self):
		return self.gender

class Student(models.Model):
	lrn=models.CharField(max_length=15, unique=True)
	fname=models.CharField(max_length=60, verbose_name="first name")
	lname=models.CharField(max_length=60, verbose_name="last name")
	mname=models.CharField(max_length=60, blank=True, verbose_name="middle name")
	ename=models.CharField(max_length=5, blank=True, verbose_name="extension name")
	gender=models.ForeignKey(Gender, on_delete=models.CASCADE, default=1)
	birth_date=models.DateField(help_text="Date format yyyy-mm-dd, e.g 2000-01-20.")
	age=models.IntegerField(default=15, help_text="Age as of first friday of June.")
	mother_tongue=models.CharField(max_length=60, default="bisaya")
	IP=models.CharField(max_length=60, help_text="Ethnic group", default="higaonon")
	religion=models.CharField(max_length=60, default="roman catholic")
	address=models.TextField(default="--student address--", help_text="Format, house#/Street/Sitio/Purok, Barangay, Municipality/City, Province")
	father_name=models.CharField(max_length=120, help_text="Format: (Last Name, First Name, Middle Name)", default="--father's name of student--", verbose_name="father's name")
	mother_name=models.CharField(max_length=120, help_text="Format: (Last Name, First Name, Middle Name)", default="--mother's name of student--", verbose_name="mother's name")
	guardian_name=models.CharField(max_length=160, default="name of student guardian", help_text="Full name of guardian", blank=True, verbose_name="guardian's name")
	relationship=models.CharField(max_length=120, default="--guardian relationship student--", blank=True)
	contact=models.CharField(max_length=13, default="--contact number--", help_text=" contact number of parents or guardian", blank=True)
	remarks=models.CharField(max_length=60, default="", help_text="")
	date_registered=models.DateTimeField(auto_now=False, auto_now_add=True)
	date_updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def full_name(self):
		fullname="%s, %s %s %s"%(self.lname, self.fname, self.mname, self.ename)
		return fullname

	def __str__(self):
		return self.full_name()