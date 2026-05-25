# AutoRent - Wypożyczalnia Samochodów Online

Aplikacja Django do zarządzania wynajmem samochodów z panelem administracyjnym.

## Wymagania

- Python 3.10+

## Instalacja i Uruchomienie

### 1. Klonowanie repozytorium
```bash
git clone https://github.com/M1K3N/autorent.git
cd autorent
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
- Tworzy konto administratora (username: `admin`, email: `admin@autorent.pl` hasło: `admin123`)
- Ładuje 20 domyślnych samochodów z obrazami

### 6. Uruchomienie serwera
```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod: `http://localhost:8000`

## Logowanie do Panelu Admina

- **Strona logowania:** http://localhost:8000/logowanie/
- **Email:** admin@autorent.pl
- **Hasło:** admin123
- **Panel admina:** http://localhost:8000/panel-admina/

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
- 💳 Wybór metody płatności (BLIK, Karta, Przelew) - proces płatności fikcyjny - omijany
- 📊 Historia rezerwacji w profilu
- ❌ Anulowanie rezerwacji

### Dla Administratora
- 🔐 Dostęp do panelu administracyjnego (`/panel-admina/`)
- ➕ Dodawanie nowych pojazdów
- ✏️ Edytowanie istniejących pojazdów (w tym zdjęcia)
- 🗑️ Usuwanie pojazdów

## Dodatkowe Komendy

### Tworzenie dodatkowych administratorów
```bash
python manage.py create_admin --username nazwa_admina --email email@example.com --password haslo123
```

## Notatki Techniczne

- **Baza danych:** SQLite (db.sqlite3)
- **Framework:** Django 6.0.5
- **Auth:** Wbudowany system użytkowników Django
- **Media:** Zdjęcia przechowywane w folderze `media/cars/`
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

## Autor
Jakub Mika - backend
Kacper Łukasiewicz - frontend
