from django.db import models
from polymorphic.models import PolymorphicModel


class HasOwnerPolymorphic(PolymorphicModel):
    owner=models.OneToOneField("models.AuthenticatedUser",on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


