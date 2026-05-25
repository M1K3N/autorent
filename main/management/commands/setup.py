from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Profile, Car
from main.views import DEFAULT_CARS


class Command(BaseCommand):
    help = 'Inicjalizuje projekt: tworzy admina i domyślne samochody'

    def handle(self, *args, **options):
        # Krok 1: Tworzenie admina
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.WARNING('✓ Admin "admin" już istnieje'))
        else:
            user = User.objects.create_user(
                username='admin',
                email='admin@autorent.pl',
                password='admin123',
                is_staff=True,
                is_superuser=True
            )
            Profile.objects.create(user=user)
            self.stdout.write(
                self.style.SUCCESS('✓ Admin "admin" został utworzony')
            )
            self.stdout.write(f'  Email: admin@autorent.pl')
            self.stdout.write(f'  Hasło: admin123')

        # Krok 2: Ładowanie domyślnych samochodów
        if Car.objects.exists():
            self.stdout.write(self.style.WARNING(f'✓ Baza zawiera już {Car.objects.count()} samochodów'))
        else:
            created_count = 0
            for car_data in DEFAULT_CARS:
                car, created = Car.objects.get_or_create(
                    slug=car_data['slug'],
                    defaults=car_data
                )
                if created:
                    created_count += 1

            self.stdout.write(
                self.style.SUCCESS(f'✓ Załadowano {created_count} domyślnych samochodów')
            )

        self.stdout.write(self.style.SUCCESS('\n✅ Setup projektu ukończony!'))
        self.stdout.write('\nMożesz teraz uruchomić: python manage.py runserver')
