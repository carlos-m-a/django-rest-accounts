from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import EmailVerification, RegistrationRequest, RegistrationRequestStates

User = get_user_model()

@receiver(post_save, sender=User)
def create_email_verification(sender, instance, created, **kwargs):
    if created:
        EmailVerification.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_registration_request(sender, instance, created, **kwargs):
    if created:
        RegistrationRequest.objects.create(user=instance)

@receiver(post_save, sender=RegistrationRequest)
def update_user(sender, instance:RegistrationRequest, created, **kwargs):
    if instance.status == RegistrationRequestStates.ACCEPTED:
        instance.user.is_active = True
        instance.user.save()
    else:
        instance.user.is_active = False
        instance.user.save()