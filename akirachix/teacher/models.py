from django.db import models

class Teacher(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.CharField(max_length=20)
	email = models.EmailField(max_length=70)
	phone_number = models.CharField(max_length=20)
	profession = models.CharField(max_length=50,null=True)
	date_employed = models.DateField(null=True)
	id_number = models.IntegerField(null=True)
	image = models.ImageField(upload_to = "profile_pictures", blank = True)

	def __str__(self):
		return self.first_name
# Create your models here.
