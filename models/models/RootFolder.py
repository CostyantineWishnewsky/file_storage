from django.db import models

class RootFolder(models.Model):
    owner=models.OneToOneField("models.AuthenticatedUser",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

