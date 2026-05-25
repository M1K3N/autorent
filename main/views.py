from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarForm, ReservationForm, UserRegistrationForm
from .models import Car, Profile, Reservation

from django.db.models import Q


# Domyślne samochody - ładowane przez management command setup
DEFAULT_CARS = [
    {
        'brand': 'BMW',
        'model_name': 'Seria 1',
        'year': 2023,
        'engine': '1.5 Benzyna',
        'transmission': 'Manualna',
        'car_type': 'Hatchback',
        'power': '140 KM',
        'seats': 5,
        'price_per_day': 180.00,
        'image': 'cars/bmw-seria-1.jpg',
        'is_available': True,
        'slug': 'bmw-seria-1-2023',
    },
    {
        'brand': 'BMW',
        'model_name': 'Seria 3',
        'year': 2024,
        'engine': '2.0 Diesel',
        'transmission': 'Automatyczna',
        'car_type': 'Sedan',
        'power': '190 KM',
        'seats': 5,
        'price_per_day': 320.00,
        'image': 'cars/bmw-seria-3.jpg',
        'is_available': True,
        'slug': 'bmw-seria-3-2024',
    },
    {
        'brand': 'BMW',
        'model_name': 'XM',
        'year': 2025,
        'engine': 'Hybryda Plug-in',
        'transmission': 'Automatyczna',
        'car_type': 'SUV Premium',
        'power': '653 KM',
        'seats': 5,
        'price_per_day': 950.00,
        'image': 'cars/bmw-xm.jpg',
        'is_available': True,
        'slug': 'bmw-xm-2025',
    },
    {
        'brand': 'Audi',
        'model_name': 'A3',
        'year': 2023,
        'engine': '1.5 Benzyna',
        'transmission': 'Manualna',
        'car_type': 'Hatchback',
        'power': '150 KM',
        'seats': 5,
        'price_per_day': 190.00,
        'image': 'cars/audi-a3.jpg',
        'is_available': True,
        'slug': 'audi-a3-2023',
    },
    {
        'brand': 'Audi',
        'model_name': 'A5',
        'year': 2024,
        'engine': '2.0 Diesel',
        'transmission': 'Automatyczna',
        'car_type': 'Coupe',
        'power': '204 KM',
        'seats': 5,
        'price_per_day': 390.00,
        'image': 'cars/audi-a5.jpg',
        'is_available': True,
        'slug': 'audi-a5-2024',
    },
    {
        'brand': 'Audi',
        'model_name': 'Q8',
        'year': 2025,
        'engine': '3.0 Benzyna',
        'transmission': 'Automatyczna',
        'car_type': 'SUV Premium',
        'power': '340 KM',
        'seats': 5,
        'price_per_day': 870.00,
        'image': 'cars/audi-q8.jpg',
        'is_available': True,
        'slug': 'audi-q8-2025',
    },
    {
        'brand': 'Toyota',
        'model_name': 'Yaris',
        'year': 2023,
        'engine': 'Hybryda',
        'transmission': 'Manualna',
        'car_type': 'Hatchback',
        'power': '116 KM',
        'seats': 5,
        'price_per_day': 140.00,
        'image': 'cars/toyota-yaris.jpg',
        'is_available': True,
        'slug': 'toyota-yaris-2023',
    },
    {
        'brand': 'Toyota',
        'model_name': 'Corolla',
        'year': 2024,
        'engine': 'Hybryda',
        'transmission': 'Automatyczna',
        'car_type': 'Sedan',
        'power': '140 KM',
        'seats': 5,
        'price_per_day': 240.00,
        'image': 'cars/toyota-corolla.jpg',
        'is_available': True,
        'slug': 'toyota-corolla-2024',
    },
    {
        'brand': 'Toyota',
        'model_name': 'RAV4',
        'year': 2025,
        'engine': 'Hybryda',
        'transmission': 'Automatyczna',
        'car_type': 'SUV',
        'power': '218 KM',
        'seats': 5,
        'price_per_day': 420.00,
        'image': 'cars/toyota-rav4.jpg',
        'is_available': True,
        'slug': 'toyota-rav4-2025',
    },
    {
        'brand': 'Volkswagen',
        'model_name': 'Polo',
        'year': 2022,
        'engine': '1.0 Benzyna',
        'transmission': 'Manualna',
        'car_type': 'Hatchback',
        'power': '95 KM',
        'seats': 5,
        'price_per_day': 150.00,
        'image': 'cars/volk-polo.jpg',
        'is_available': True,
        'slug': 'volkswagen-polo-2022',
    },
    {
        'brand': 'Volkswagen',
        'model_name': 'Passat',
        'year': 2024,
        'engine': '2.0 Diesel',
        'transmission': 'Automatyczna',
        'car_type': 'Sedan',
        'power': '200 KM',
        'seats': 5,
        'price_per_day': 290.00,
        'image': 'cars/volk-passat.jpg',
        'is_available': True,
        'slug': 'volkswagen-passat-2024',
    },
    {
        'brand': 'Volkswagen',
        'model_name': 'Touareg',
        'year': 2025,
        'engine': '3.0 Diesel',
        'transmission': 'Automatyczna',
        'car_type': 'SUV Premium',
        'power': '286 KM',
        'seats': 5,
        'price_per_day': 560.00,
        'image': 'cars/volk-touareg.jpg',
        'is_available': True,
        'slug': 'volkswagen-touareg-2025',
    },
    {
        'brand': 'Honda',
        'model_name': 'Jazz',
        'year': 2023,
        'engine': '1.3 Benzyna',
        'transmission': 'Manualna',
        'car_type': 'Hatchback',
        'power': '102 KM',
        'seats': 5,
        'price_per_day': 130.00,
        'image': 'cars/honda-jazz.jpg',
        'is_available': True,
        'slug': 'honda-jazz-2023',
    },
    {
        'brand': 'Honda',
        'model_name': 'Civic',
        'year': 2024,
        'engine': '1.5 Benzyna',
        'transmission': 'Automatyczna',
        'car_type': 'Sedan',
        'power': '182 KM',
        'seats': 5,
        'price_per_day': 220.00,
        'image': 'cars/honda-civic.jpg',
        'is_available': True,
        'slug': 'honda-civic-2024',
    },
    {
        'brand': 'Honda',
        'model_name': 'Prelude',
        'year': 2025,
        'engine': '2.0 Benzyna',
        'transmission': 'Manualna',
        'car_type': 'Coupe Sport',
        'power': '220 KM',
        'seats': 2,
        'price_per_day': 460.00,
        'image': 'cars/honda-prelude.jpg',
        'is_available': True,
        'slug': 'honda-prelude-2025',
    },
    {
        'brand': 'Renault',
        'model_name': 'Clio',
        'year': 2022,
        'engine': '1.0 Benzyna',
        'transmission': 'Manualna',
        'car_type': 'Hatchback',
        'power': '95 KM',
        'seats': 5,
        'price_per_day': 130.00,
        'image': 'cars/reno-clio.jpg',
        'is_available': True,
        'slug': 'renault-clio-2022',
    },
    {
        'brand': 'Renault',
        'model_name': 'Megane',
        'year': 2024,
        'engine': '1.6 Diesel',
        'transmission': 'Manualna',
        'car_type': 'Sedan',
        'power': '130 KM',
        'seats': 5,
        'price_per_day': 150.00,
        'image': 'cars/reno-megane.jpg',
        'is_available': True,
        'slug': 'renault-megane-2024',
    },
    {
        'brand': 'Renault',
        'model_name': 'Alpine',
        'year': 2025,
        'engine': '1.8 Turbo Benzyna',
        'transmission': 'Automatyczna',
        'car_type': 'Coupe Sport',
        'power': '300 KM',
        'seats': 2,
        'price_per_day': 720.00,
        'image': 'cars/reno-alpine.jpg',
        'is_available': True,
        'slug': 'renault-alpine-2025',
    },
    {
        'brand': 'Mercedes',
        'model_name': 'Klasa A',
        'year': 2023,
        'engine': '1.3 Benzyna',
        'transmission': 'Automatyczna',
        'car_type': 'Hatchback',
        'power': '136 KM',
        'seats': 5,
        'price_per_day': 310.00,
        'image': 'cars/mercedes-klasa-a.jpg',
        'is_available': True,
        'slug': 'mercedes-klasa-a-2023',
    },
    {
        'brand': 'Mercedes',
        'model_name': 'Klasa C',
        'year': 2024,
        'engine': '2.0 Diesel',
        'transmission': 'Automatyczna',
        'car_type': 'Sedan Premium',
        'power': '200 KM',
        'seats': 5,
        'price_per_day': 490.00,
        'image': 'cars/mercedes-klasa-c.jpg',
        'is_available': True,
        'slug': 'mercedes-klasa-c-2024',
    },
    {
        'brand': 'Mercedes',
        'model_name': 'GLE',
        'year': 2025,
        'engine': '3.0 Diesel',
        'transmission': 'Automatyczna',
        'car_type': 'SUV Premium',
        'power': '330 KM',
        'seats': 5,
        'price_per_day': 690.00,
        'image': 'cars/mercedes-gle.jpg',
        'is_available': True,
        'slug': 'mercedes-gle-2025',
    },
]


def home(request):
    featured = Car.objects.filter(is_available=True).order_by('-price_per_day')[:3]
    types = Car.objects.values_list('car_type', flat=True).distinct().order_by('car_type')
    return render(request, 'main/index.html', {'featured_cars': featured, 'types': types})


def cars(request):

    queryset = Car.objects.filter(is_available=True)

    brand = request.GET.get('brand', '').strip()
    car_type = request.GET.get('type', '').strip()
    pickup_date = request.GET.get('pickup_date', '').strip()
    return_date = request.GET.get('return_date', '').strip()

    if brand:
        queryset = queryset.filter(brand__iexact=brand)

    if car_type:
        queryset = queryset.filter(car_type__icontains=car_type)

    date_filter_error = False

    if pickup_date or return_date:
        if not pickup_date or not return_date:
            messages.error(request, 'Wybierz zarówno datę odbioru, jak i datę zwrotu.')
            date_filter_error = True
        elif return_date < pickup_date:
            messages.error(request, 'Data zwrotu nie może być wcześniejsza niż data odbioru.')
            date_filter_error = True
        else:
            reserved_car_ids = Reservation.objects.filter(
                status__in=['created', 'confirmed'],
                pickup_date__lte=return_date,
                return_date__gte=pickup_date,
            ).values_list('car_id', flat=True)

            queryset = queryset.exclude(id__in=reserved_car_ids)

    brands = Car.objects.values_list('brand', flat=True).distinct().order_by('brand')
    types = Car.objects.values_list('car_type', flat=True).distinct().order_by('car_type')

    return render(request, 'main/samochody.html', {
        'cars': queryset,
        'brands': brands,
        'types': types,
        'selected_brand': brand,
        'selected_type': car_type,
        'selected_pickup_date': pickup_date,
        'selected_return_date': return_date,
        'date_filter_error': date_filter_error,
    })


def detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    similar = Car.objects.filter(car_type=car.car_type).exclude(pk=car.pk)[:3]
    return render(request, 'main/szczegoly-pojazdu.html', {'car': car, 'similar': similar})


@login_required
def reservation(request, slug=None):
    car = get_object_or_404(Car, slug=slug) if slug else None

    if car and not car.is_available:
        messages.error(request, 'Ten samochód jest aktualnie niedostępny.')
        return redirect('detail', slug=car.slug)

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            pickup_date = form.cleaned_data.get('pickup_date')
            return_date = form.cleaned_data.get('return_date')

            overlapping_reservation = Reservation.objects.filter(
                car=car,
                status__in=['created', 'confirmed'],
                pickup_date__lte=return_date,
                return_date__gte=pickup_date,
            ).exists()

            if overlapping_reservation:
                messages.error(
                    request,
                    'Ten samochód jest już zarezerwowany w wybranym terminie. Wybierz inne daty.'
                )
                return render(request, 'main/rezerwacja.html', {
                    'form': form,
                    'car': car,
                })

            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.car = car
            reservation.status = 'confirmed'
            reservation.save()

            messages.success(request, 'Rezerwacja została utworzona pomyślnie.')
            return redirect('profile')
        else:
            messages.error(request, 'Nie udało się utworzyć rezerwacji. Sprawdź poprawność danych.')
    else:
        form = ReservationForm()

    return render(request, 'main/rezerwacja.html', {
        'form': form,
        'car': car,
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        username = username_or_email

        if username_or_email and '@' in username_or_email:
            user_obj = User.objects.filter(email__iexact=username_or_email).first()
            if user_obj:
                username = user_obj.username

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Zalogowano pomyślnie.')
            return redirect('home')
        else:
            messages.error(request, 'Nieprawidłowy login lub hasło.')

    return render(request, 'main/logowanie.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone', ''),
                address=form.cleaned_data.get('address', ''),
            )
            login(request, user)
            messages.success(request, 'Konto utworzone. Jesteś zalogowany.')
            return redirect('home')
        else:
            messages.error(request, 'Błąd przy tworzeniu konta. Sprawdź dane.')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/rejestracja.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    reservations = Reservation.objects.filter(user=request.user)
    profile = getattr(request.user, 'profile', None)
    return render(request, 'main/profil.html', {
        'reservations': reservations,
        'profile': profile,
    })


@login_required
def admin_panel(request):
    if not request.user.is_staff:
        return render(request, 'main/panel-admina.html', {'error': 'Dostęp tylko dla administratora.'})
    cars = Car.objects.all()
    reservations = Reservation.objects.order_by('-created_at')[:10]
    return render(request, 'main/panel-admina.html', {
        'cars': cars,
        'reservations': reservations,
    })


@login_required
def car_create(request):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = CarForm()
    return render(request, 'main/car_form.html', {'form': form, 'title': 'Dodaj pojazd'})


@login_required
def car_update(request, slug):
    if not request.user.is_staff:
        return redirect('home')
    car = get_object_or_404(Car, slug=slug)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = CarForm(instance=car)
    return render(request, 'main/car_form.html', {'form': form, 'title': 'Edytuj pojazd'})


@login_required
def car_delete(request, slug):
    if not request.user.is_staff:
        return redirect('home')
    car = get_object_or_404(Car, slug=slug)
    if request.method == 'POST':
        car.delete()
        return redirect('admin_panel')
    return render(request, 'main/car_delete.html', {'car': car})
