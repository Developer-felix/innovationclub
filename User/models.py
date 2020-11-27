<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	user_image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	def __str__(self):
		return f' {self.user.username} Profile'
=======
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	user_image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	def __str__(self):
		return f' {self.user.username} Profile'
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.user_image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.user_image.path)
>>>>>>> 62f240d3c46a6af1f386a4008cf2a2700675bf03
