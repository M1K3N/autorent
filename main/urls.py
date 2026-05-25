from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('samochody/<slug:slug>/', views.detail, name='detail'),
    path('samochody/', views.cars, name='cars'),
    path('rezerwacja/<slug:slug>/', views.reservation, name='reservation'),
    path('rezerwacja/', views.reservation, name='reservation'),
    path('logowanie/', views.login_view, name='login'),
    path('rejestracja/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('panel-admina/', views.admin_panel, name='admin_panel'),
    path('panel-admina/dodaj/', views.car_create, name='car_create'),
    path('panel-admina/edytuj/<slug:slug>/', views.car_update, name='car_update'),
    path('panel-admina/usun/<slug:slug>/', views.car_delete, name='car_delete'),
    path('profil/', views.profile, name='profile'),
    path('rezerwacja/anuluj/<int:pk>/', views.reservation_delete, name='reservation_delete'),
]
