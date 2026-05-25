# AutoRent - Wypożyczalnia Samochodów Online

Aplikacja Django do zarządzania wynajmem samochodów z panelem administracyjnym.

## Wymagania

- Python 3.10+
- Django 6.0.5
- Pillow (do obsługi ImageField)

## Instalacja i Uruchomienie

### 1. Klonowanie repozytorium
```bash
git clone <url-repozytorium>
cd Autorent
```

### 2. Tworzenie wirtualnego środowiska
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalacja zależności
```bash
pip install -r requirements.txt
```

### 4. Migracja bazy danych
```bash
python manage.py migrate
```

### 5. Inicjalizacja danych
```bash
python manage.py setup
```

Ta komenda automatycznie:
- Tworzy konto administratora (username: `admin`, hasło: `admin123`)
- Ładuje 20 domyślnych samochodów z obrazami

### 6. Uruchomienie serwera
```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod: `http://localhost:8000`

## Logowanie do Panelu Admina

- **Strona logowania:** http://localhost:8000/logowanie/
- **Username:** admin (lub **Email:** admin@autorent.pl)
- **Hasło:** admin123
- **Panel admina:** http://localhost:8000/panel-admina/

Możesz się zalogować używając **nazwy użytkownika** lub **adresu email**.

## Struktura Projektu

```
Autorent/
├── autorent/          # Konfiguracja projektu Django
├── main/              # Główna aplikacja
│   ├── models.py      # Modele bazy danych (Car, Reservation, Profile)
│   ├── views.py       # Widoki aplikacji
│   ├── forms.py       # Formularze
│   ├── urls.py        # Routing URLs
│   ├── static/        # Pliki statyczne (CSS, obrazy)
│   ├── templates/     # Szablony HTML
│   ├── migrations/    # Migracje bazy danych
│   └── management/    # Komendy zarządzania
├── media/             # Wgrane zdjęcia samochodów
├── manage.py          # Punkt wejścia Django
└── requirements.txt   # Zależności projektów
```

## Funkcje Aplikacji

### Dla Użytkowników
- 👤 Rejestracja i logowanie
- 🚗 Przeglądanie dostępnych samochodów
- 📅 Rezerwacja samochodów na wybrane daty
- 💳 Wybór metody płatności (BLIK, Karta, Przelew)
- 📊 Historia rezerwacji w profilu
- ❌ Anulowanie rezerwacji

### Dla Administratora
- 🔐 Dostęp do panelu administracyjnego (`/panel-admina/`)
- ➕ Dodawanie nowych pojazdów
- ✏️ Edytowanie istniejących pojazdów (w tym zdjęcia)
- 🗑️ Usuwanie pojazdów
- 📱 Zarządzanie rezerwacjami

## Dane Logowania - Admin

## Dane Logowania - Admin

Utworzone automatycznie przez `python manage.py setup`:

| Pole | Wartość |
|------|---------|
| Username | admin |
| Email | admin@autorent.pl |
| Hasło | admin123 |

**Możesz się zalogować za pomocą username'u lub emaila!**

## Dodatkowe Komendy

### Tworzenie dodatkowych administratorów
```bash
python manage.py create_admin --username nazwa_admina --email email@example.com --password haslo123
```

## Notatki Techniczne

- **Baza danych:** SQLite (db.sqlite3)
- **Framework:** Django 6.0.5
- **Auth:** Wbudowany system użytkowników Django
- **Media:** Zdjęcia przechowywane w `media/cars/`
- **CSRF Protection:** Wdrożona na wszystkich formularzach
- **Responsywny Design:** Bootstrap-like CSS z `style.css`

## Adresy URL

| URL | Opis |
|-----|------|
| `/` | Strona główna |
| `/samochody/` | Lista wszystkich samochodów |
| `/samochody/<slug>/` | Szczegóły pojazdu |
| `/rezerwacja/<slug>/` | Formularz rezerwacji |
| `/profil/` | Profil użytkownika |
| `/logowanie/` | Logowanie |
| `/rejestracja/` | Rejestracja |
| `/panel-admina/` | Panel administracyjny (wymaga is_staff) |
| `/panel-admina/dodaj/` | Dodaj pojazd |
| `/panel-admina/edytuj/<slug>/` | Edytuj pojazd |
| `/panel-admina/usun/<slug>/` | Usuń pojazd |

## Rozwiązywanie Problemów

### Brak zdjęć samochodów
Upewnij się, że folder `media/cars/` istnieje i zawiera pliki `.jpg`.

### Błąd dostępu do panelu admin
Upewnij się, że jesteś zalogowany jako użytkownik z `is_staff=True`.

### Błędy bazy danych
Uruchom migracje ponownie:
```bash
python manage.py migrate
```

## Autor

Projekt stworzony dla celów edukacyjnych.
