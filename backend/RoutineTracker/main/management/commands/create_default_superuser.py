from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()

class Command(BaseCommand):
    help = "Creates a default superuser if none exist"

    def handle(self, *args, **kwargs):
        email = "admin@example.com"
        username = "admin"
        new_password = get_random_string(10)

        try:
            if not User.objects.filter(is_superuser=True).exists():
                self.stdout.write("No superusers found, creating one...")
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=new_password
                )
                self.stdout.write(self.style.SUCCESS("A superuser has been created"))
                self.stdout.write(f"Username: {username}")
                self.stdout.write(f"Email: {email}")
                self.stdout.write(f"Password: {new_password}")
            else:
                self.stdout.write("A superuser already exists in the database.")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"There was an error: {e}"))
