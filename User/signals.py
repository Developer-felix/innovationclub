from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance, **kwargs):
<<<<<<< HEAD
		instance.profile.save()

post_save.connect(create_profile, sender=User)
post_save.connect(save_profile, sender=User)
=======
		instance.profile.save()
>>>>>>> 62f240d3c46a6af1f386a4008cf2a2700675bf03
