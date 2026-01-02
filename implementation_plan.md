# Implementation Plan - Phase 1: Core Functionality

## Goal Description
Implement the core features of the Beauty Salon Management System as defined in the SRS Phase 1. This includes setting up the Django project structure, user authentication, service packages, and appointment booking.

## Proposed Changes

### Project Structure
#### [NEW] Apps
- `users`: For custom user model and authentication.
- `services`: For managing beauty packages.
- `appointments`: For booking logic.
- `core`: For landing pages and base templates.

### Users App
#### [NEW] Models
- `User`: Custom user model inheriting from `AbstractUser`.
  - Fields: `phone_number`, `is_customer`, `is_admin`, address fields.
#### [NEW] Views
- `RegisterView`: User registration.
- `LoginView`, `LogoutView`: Standard auth views.
- `ProfileView`: User profile management.

### Services App
#### [NEW] Models
- `ServicePackage`:
  - Fields: `name`, `description`, `price`, `duration` (minutes), `image`, `category`.
#### [NEW] Views
- `PackageListView`: Display all packages.
- `PackageDetailView`: View single package details.

### Appointments App
#### [NEW] Models
- `Appointment`:
  - Fields: `customer` (FK User), `service_package` (FK ServicePackage), `date`, `time`, `status`, `notes`.
#### [NEW] Views
- `BookingView`: Form to book an appointment.
- `AppointmentListView`: History for customers.
- `AdminAppointmentView`: Dashboard for viewing all bookings.

### UI/UX Design
- **Styling**: Vanilla CSS with a modern, responsive design (mobile-friendly).
- **Theme**: Soft, elegant colors suitable for a beauty salon (e.g., pastels, gold/rose-gold accents).

## Verification Plan

### Automated Tests
- Run `python manage.py test` to verify models and core logic.

### Manual Verification
1. **Registration/Login**: Create a customer account, login, logout.
2. **Admin**: Create a superuser, access Django Admin, add Service Packages.
3. **Booking**: As a customer, view packages, select one, pick a date/time, and book.
4. **Dashboard**: Verify the appointment shows up in the Customer and Admin dashboards.
