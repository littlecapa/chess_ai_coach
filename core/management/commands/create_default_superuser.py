from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

class Command(BaseCommand):
    help = "Creates a default superuser if none exists"

    def handle(self, *args, **options):
        User = get_user_model()
        username = getattr(settings, "DEFAULT_ADMIN_USERNAME", "admin")
        email = getattr(settings, "DEFAULT_ADMIN_EMAIL", "admin@example.com")
        password = getattr(settings, "DEFAULT_ADMIN_PASSWORD", "AdminPass123!")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f"✅ Superuser '{username}' created."))
        else:
            self.stdout.write(self.style.WARNING(f"ℹ️ Superuser '{username}' already exists."))
