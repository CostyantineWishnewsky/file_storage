from django.contrib.auth.models import AbstractUser
from django.db import models

from ..managers.AuthenticatedUserManager import AuthenticatedUserManager

class AuthenticatedUser(AbstractUser):
    username = models.CharField(max_length=50)
    root_folder=models.OneToOneField("models.RootFolder",default=None,null=True,on_delete=models.CASCADE)
    email=models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AuthenticatedUserManager()


    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True
    )

    def __str__(self):
        return self.email