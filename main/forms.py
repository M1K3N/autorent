from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import slugify

from .models import Car, Reservation, Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['pickup_date', 'return_date', 'pickup_location', 'payment_method']
        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_method': forms.Select(),
        }

    def clean(self):
        cleaned_data = super().clean()
        pickup_date = cleaned_data.get('pickup_date')
        return_date = cleaned_data.get('return_date')
        if pickup_date and return_date and return_date < pickup_date:
            raise forms.ValidationError('Data zwrotu musi być późniejsza niż data odbioru.')
        return cleaned_data


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model_name', 'year', 'engine', 'transmission', 'car_type', 'power', 'seats', 'price_per_day', 'image', 'is_available']
        widgets = {
            'image': forms.FileInput(),  # Bez clear checkbox
        }

    def save(self, commit=True):
        car = super().save(commit=False)
        base_slug = slugify(f"{car.brand} {car.model_name}")
        slug = base_slug
        counter = 1
        while Car.objects.filter(slug=slug).exclude(pk=car.pk).exists():
            counter += 1
            slug = f"{base_slug}-{counter}"
        car.slug = slug
        if commit:
            car.save()
        return car
