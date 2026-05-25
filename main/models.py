from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    seats = models.PositiveSmallIntegerField(default=5)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(
        upload_to='cars/',
        blank=True,
        help_text='Wgraj obraz samochodu'
    )
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ['brand', 'model_name', 'year']

    def __str__(self):
        return f'{self.brand} {self.model_name} ({self.year})'


class Reservation(models.Model):
    PAYMENT_CHOICES = [
        ('blik', 'BLIK'),
        ('card', 'Karta'),
        ('transfer', 'Przelew'),
    ]

    STATUS_CHOICES = [
        ('created', 'Utworzona'),
        ('confirmed', 'Potwierdzona'),
        ('cancelled', 'Anulowana'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    pickup_location = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Rezerwacja {self.car} dla {self.user.username} ({self.pickup_date} - {self.return_date})'
