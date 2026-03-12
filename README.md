# 🌸 Rose-Gold Beauty Salon Management System

A premium, fully functional Django-based web application designed for women-only beauty salons in Pakistan. This system offers an elegant user interface, seamless appointment booking, and a comprehensive admin dashboard for business operations.

---

## ✨ Features

### 👩‍🦰 For Customers
- **Authentication**: Secure registration and login with Pakistani phone number validation (+92-XXX-XXXXXXX).
- **Service Catalog**: Browse categorized service packages (Bridal, Hair Care, Skin Care, Makeup) with pricing and durations.
- **Appointment Booking**: Intuitive booking system with date and time selection (enforcing business hours 10 AM - 8 PM).
- **Personal Dashboard**: View upcoming appointments, booking history, and personalized service recommendations.
- **Bilingual Support**: Fully internationalized with **English and Urdu** language switching.
- **Responsive Design**: Optimized for mobile devices, ensuring accessibility for all users.

### 👩‍💼 For Administrators
- **Admin Dashboard**: Real-time overview of business performance, including:
  - Total Revenue Tracking (PKR).
  - Appointment Status Stats (Pending, Confirmed, Completed, Cancelled).
- **Appointment Management**: Confirm bookings, mark as completed, or cancel with automatic slot updates.
- **Package Management**: CRUD operations for service packages, including image uploads and pricing updates.
- **Search & Filter**: Find appointments quickly by customer name, phone, or email.

---

## 🛠️ Technology Stack

- **Backend**: Django 5.2.7 (Python)
- **Database**: SQLite (Development) / PostgreSQL (Production ready)
- **Frontend**: Vanilla HTML5, CSS3 (Custom Design System), JavaScript
- **Internationalization**: Django I18N (i18n)
- **Security**: CSRF protection, Hashed passwords (PBKDF2), Role-based access control.

---

## 🚀 Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/RAAZIA-YASIN6770/Beauty-Salon-Management-System.git
cd Beauty-Salon-Management-System
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations & Setup Database
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📂 Project Structure

- `core/`: Homepage, Contact, and About pages.
- `users/`: Custom User model, registration, and profile management.
- `services/`: Service packages and category management.
- `appointments/`: Booking logic, slot management, and admin dashboard.
- `templates/`: Global and app-specific Django templates with Rose-Gold styling.
- `static/`: Custom CSS design system and frontend assets.

---

## 🇵🇰 Pakistan-Specific Settings

The system is pre-configured for the local market:
- **Currency**: Pakistani Rupee (PKR).
- **Timezone**: Asia/Karachi (PST).
- **Phone Format**: +92-XXX-XXXXXXX validation.
- **Business Hours**: 10:00 AM to 8:00 PM (Configurable).

---

## 🗺️ Roadmap
- [ ] SMS/Email Notifications for appointment confirmations.
- [ ] Professional Calendar View for Admin.
- [ ] Manual "Walk-in" booking for staff.
- [ ] Automated daily database backups.

---

## 🤝 Contribution
Contributions are welcome! If you have suggestions or want to fix a bug, feel free to open an issue or submit a pull request.

## 📝 License
This project is for educational and business management purposes.

---
**Developed with ❤️ for the Women of Pakistan.**