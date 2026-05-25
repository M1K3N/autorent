from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField()),
                ('engine', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=50)),
                ('car_type', models.CharField(max_length=50)),
                ('power', models.CharField(max_length=50)),
                ('seats', models.PositiveSmallIntegerField(default=5)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(blank=True, help_text='Wgraj obraz samochodu', upload_to='cars/')),
                ('is_available', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'ordering': ['brand', 'model_name', 'year'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateField()),
                ('return_date', models.DateField()),
                ('pickup_location', models.CharField(max_length=255)),
                ('payment_method', models.CharField(choices=[('blik', 'BLIK'), ('card', 'Karta'), ('transfer', 'Przelew')], max_length=20)),
                ('status', models.CharField(choices=[('created', 'Utworzona'), ('confirmed', 'Potwierdzona'), ('cancelled', 'Anulowana')], default='created', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
