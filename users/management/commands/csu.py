from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            telegram_name='ilya_evl',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('0000')
        user.save()
        print('superuser created')