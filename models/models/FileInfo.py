from django.db import models
from models.models.HasOwnerPolymorphic import HasOwnerPolymorphic


class FileInfo(HasOwnerPolymorphic):
    class FileInfoHasParentType(models.TextChoices):
        ROOT_FOLDER = "root_folder"
        FOLDER = "folder"
    name=models.CharField(max_length=255)
    path_in_storage=models.CharField(max_length=255)
    parent=models.CharField(max_length=12,choices=FileInfoHasParentType.choices)