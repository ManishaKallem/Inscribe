from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, help_text=_("The username of the user."))
    email = models.EmailField(help_text=_("The email address of the user."), unique=True)
    first_name = models.CharField(
        help_text=_("The first name of the user"), max_length=100
    )
    last_name = models.CharField(
        help_text=_("The last name of the user"), max_length=100
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = managers.CustomUserManager()

    class Meta:
        ordering = ("id",)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name}'s account"
