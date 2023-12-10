from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model 
from .models import Profile
from .tasks import send_profile_creation_confirmation

User = get_user_model()

# create user profile upon user creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print(f'Profile created for: {instance}')
    if created:
        try:
            p = Profile.objects.create(user=instance)
            p.save()
            print(p)
            send_profile_creation_confirmation.delay(p.user.email)
        except Exception as e:
            print(e)