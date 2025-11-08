from django.apps import AppConfig


class ModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models'

    def ready(self):
        from .models.AuthenticatedUser import AuthenticatedUser
        from .models.RootFolder import RootFolder
        from .models.FileInfo import FileInfo
        from .models.FolderInfo import FolderInfo
        
        
