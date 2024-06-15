from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    introduction = models.TextField(blank=True, null=True)
    # Other profile stuffs will come here....

    def __str__(self):
        return self.user.username


# To locate user is inactivated
@receiver(pre_save, sender=Profile)
def user_to_inactive(sender, instance, *args, **kwargs):
    # It will be activated by superuser.
    instance.user.is_active = False
    instance.user.save()
