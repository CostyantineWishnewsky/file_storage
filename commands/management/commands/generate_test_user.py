from typing import Any
from django.core.management.base import BaseCommand
# from django.contrib.auth import get_user_model

# User=get_user_model()
from models.models.AuthenticatedUser import AuthenticatedUser


class Command(BaseCommand):
    help = f"Generate test user with email 'email1@gmail.com' and password 'password123"


    def add_arguments(self, parser):
        pass

    def handle(self, *args: Any, **options: Any):
        # user=User.objects.create_user(
        user=AuthenticatedUser.objects.create_user(
            username='user1',
            email='email1@gmail.com',
            password= 'password123',
            last_name='last_name1',
        )
        self.stdout.write(self.style.SUCCESS(f"✅ Successfully test user has been created!"))
        
