from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Profile


class Command(BaseCommand):
    help = 'Tworzy konto administratora'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Username admina (default: admin)'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@autorent.pl',
            help='Email admina (default: admin@autorent.pl)'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='admin123',
            help='Hasło admina (default: admin123)'
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Użytkownik "{username}" już istnieje!')
            )
            return

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )

        # Tworzy profil
        Profile.objects.create(user=user)

        self.stdout.write(
            self.style.SUCCESS(
                f'✓ Admin "{username}" utworzony pomyślnie!\n'
                f'  Email: {email}\n'
                f'  Hasło: {password}'
            )
        )
