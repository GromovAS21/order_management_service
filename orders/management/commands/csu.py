import os

import django
from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Создание суперпользователя"""

    def handle(self, *args, **options):
        try:
            user = User.objects.create_superuser(
                username=os.getenv("ADMIN_USERNAME"),
            )
            user.set_password(os.getenv("ADMIN_PASSWORD"))
            user.save()
        except django.db.utils.IntegrityError:
            self.stdout.write(self.style.ERROR("SUPERUSER ALREADY CREATED"))
        except Exception:
            self.stdout.write(self.style.ERROR("SUPERUSER CREATE FAILED"))
        else:
            self.stdout.write(self.style.SUCCESS("SUPERUSER CREATE SUCCESS"))
