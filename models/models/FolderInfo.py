from django.db import models
from models.models.HasOwnerPolymorphic import HasOwnerPolymorphic

class FolderInfo(HasOwnerPolymorphic):
    class FolderInfoHasParentType(models.TextChoices):
        ROOT_FOLDER = "root_folder"
        FOLDER = "folder"
    name=models.CharField(max_length=255)
    parent=models.CharField(max_length=12,choices=FolderInfoHasParentType.choices)
    