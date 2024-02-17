from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings


class User(AbstractUser): 
    email = models.EmailField(
        _("email address"),
        max_length=254,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
        blank=False,
        null=False
    )


class RegistrationRequestStates():
    REQUESTED = 1
    ACCEPTED = 2
    REJECTED = 3


class RegistrationRequest(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='email_verification'
    )
    status = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)


class EmailVerification(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='email_verification'
    )
    is_verified = models.BooleanField(
        null=False, 
        default=False
    )
    verification_date = models.DateTimeField(
        null=True
    )
    def __str__(self):
        return self.user.email


class EmailVerificationCode(models.Model):
    email = models.EmailField(
        max_length=254,
        unique=True,
        error_messages={
            "unique": "A verification with that email already exists.",
        },
        blank=False,
        null=False
    )
    code = models.PositiveIntegerField(
        null=False, 
        default=0
    )
    attempt_count = models.PositiveSmallIntegerField(
        null=False, 
        default=0
    )
    sent_date = models.DateTimeField(
        null=False
    )

    def __str__(self):
        return self.email