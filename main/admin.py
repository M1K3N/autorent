from django.contrib import admin

from .models import Car, Profile, Reservation


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username', 'user__email', 'phone')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'year', 'car_type', 'price_per_day', 'is_available')
    prepopulated_fields = {'slug': ('brand', 'model_name')}
    search_fields = ('brand', 'model_name', 'engine', 'car_type')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('car', 'user', 'pickup_date', 'return_date', 'payment_method', 'status')
    list_filter = ('status', 'payment_method')
    search_fields = ('user__username', 'car__brand', 'car__model_name')
