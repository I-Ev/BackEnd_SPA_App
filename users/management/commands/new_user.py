from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            telegram_name='test_user',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('0000')
        user.save()
        print('[########## user created #########]')