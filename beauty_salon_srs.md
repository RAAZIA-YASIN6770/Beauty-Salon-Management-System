# Software Requirements Specification (SRS)
## Beauty Salon Management System

**Version:** 1.0  
**Date:** December 20, 2025  
**Prepared for:** Women's Beauty Salon, Pakistan  
**Prepared by:** Software Engineering Team

---

## 1. Introduction

### 1.1 Purpose
This document specifies the software requirements for a web-based Beauty Salon Management System designed for a women-only beauty salon operating in a small town in Pakistan. The system will enable customers to book appointments online and view service packages, while allowing salon administrators to manage appointments and operations.

### 1.2 Scope
The Beauty Salon Management System is a Django-based web application that will provide the following capabilities:

**For Customers:**
- User registration and authentication
- Appointment booking and management
- Service package browsing
- Appointment history viewing

**For Administrators:**
- Admin dashboard access
- Comprehensive appointment management
- Customer information viewing
- Service package management

### 1.3 Definitions and Acronyms
- **SRS:** Software Requirements Specification
- **UI:** User Interface
- **Admin:** Administrator/Salon Owner
- **Customer:** End user who books appointments
- **Package:** Bundle of beauty services offered together

### 1.4 References
- Django Framework Documentation (v4.x or higher)
- Python 3.8+ Documentation
- Web Content Accessibility Guidelines (WCAG) 2.1

### 1.5 Overview
This document is organized into functional requirements, non-functional requirements, system features, external interface requirements, and other specifications necessary for development.

---

## 2. Overall Description

### 2.1 Product Perspective
This is a standalone web application that will serve as the primary digital interface between the beauty salon and its customers. The system will be accessible via web browsers on desktop and mobile devices.

### 2.2 Product Functions
The major functions include:
- User authentication and authorization (customer and admin roles)
- Appointment scheduling with date and time selection
- Service package catalog with descriptions and pricing
- Appointment management dashboard for administrators
- Customer profile management
- Notification system for appointment confirmations

### 2.3 User Classes and Characteristics

**Customer (Primary User):**
- Women from local community
- Varying technical expertise levels
- Primary language: Urdu/English
- Mobile and desktop access
- Age range: 16-60 years

**Administrator (Salon Owner/Staff):**
- Salon owner or designated staff member
- Moderate technical skills
- Requires comprehensive appointment oversight
- Desktop/tablet access primarily
- Manages daily salon operations

### 2.4 Operating Environment
- **Platform:** Web-based application
- **Server:** Linux/Windows server environment
- **Framework:** Django 4.x+
- **Database:** PostgreSQL or SQLite (for initial deployment)
- **Client:** Modern web browsers (Chrome, Firefox, Safari, Edge)
- **Network:** Internet connectivity required

### 2.5 Design and Implementation Constraints
- Must be developed using Django framework
- Should support Urdu and English languages
- Must be responsive for mobile devices (prevalent in small towns)
- Should work on low-bandwidth connections
- Must comply with data protection requirements
- Budget constraints typical of small business operations

### 2.6 Assumptions and Dependencies
- Salon has reliable internet connectivity
- Admin staff has basic computer literacy
- Customers have access to smartphones or computers
- Email/SMS services available for notifications
- Hosting environment will be provided

---

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Management

**FR-1.1: Customer Registration**
- The system shall allow new customers to register with email, phone number, full name, and password
- The system shall validate email format and phone number format (Pakistan: +92-XXX-XXXXXXX)
- The system shall send verification email/SMS upon registration
- The system shall prevent duplicate registrations using the same email or phone number

**FR-1.2: Customer Login**
- The system shall authenticate customers using email/phone and password
- The system shall provide "Forgot Password" functionality
- The system shall maintain user sessions securely
- The system shall allow customers to logout

**FR-1.3: Admin Login**
- The system shall provide separate admin login interface
- The system shall authenticate admin users with username and password
- The system shall restrict admin panel access to authorized users only
- The system shall support admin session management

**FR-1.4: Profile Management**
- Customers shall be able to view and edit their profile information
- Customers shall be able to change their password
- The system shall maintain customer contact history

#### 3.1.2 Appointment Management

**FR-2.1: Appointment Booking**
- Customers shall be able to select date and time for appointments
- The system shall display available time slots based on salon working hours
- The system shall prevent double-booking of time slots
- Customers shall be able to select specific services or packages
- The system shall provide appointment confirmation message
- The system shall send confirmation notification (email/SMS)

**FR-2.2: Appointment Viewing**
- Customers shall be able to view all their upcoming appointments
- Customers shall be able to view their appointment history
- Each appointment shall display date, time, services, and status

**FR-2.3: Appointment Modification**
- Customers shall be able to cancel appointments (with minimum notice period)
- Customers shall be able to reschedule appointments (subject to availability)
- The system shall update appointment status accordingly

**FR-2.4: Admin Appointment Management**
- Admin shall be able to view all appointments in calendar/list view
- Admin shall be able to filter appointments by date, customer, or status
- Admin shall be able to confirm, reschedule, or cancel appointments
- Admin shall be able to mark appointments as completed
- Admin shall be able to add manual appointments for walk-in customers

#### 3.1.3 Service Package Management

**FR-3.1: Package Display**
- The system shall display all available service packages to customers
- Each package shall include name, description, services included, duration, and price
- Packages shall be organized in categories (e.g., Bridal, Hair Care, Skin Care, Makeup)
- The system shall display package images where available

**FR-3.2: Package Management (Admin)**
- Admin shall be able to create new service packages
- Admin shall be able to edit existing package details
- Admin shall be able to activate/deactivate packages
- Admin shall be able to set package pricing in PKR
- Admin shall be able to upload package images

#### 3.1.4 Dashboard and Reporting

**FR-4.1: Customer Dashboard**
- Customers shall see upcoming appointments summary upon login
- Dashboard shall display recommended packages
- Dashboard shall show appointment statistics

**FR-4.2: Admin Dashboard**
- Admin shall see daily appointment summary
- Admin shall see weekly/monthly booking statistics
- Admin shall view list of today's appointments
- Admin shall see new customer registrations
- Admin shall access quick actions for common tasks

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance Requirements
- **NFR-1.1:** System shall load pages within 3 seconds on average internet connection
- **NFR-1.2:** System shall support at least 50 concurrent users
- **NFR-1.3:** Database queries shall execute within 2 seconds
- **NFR-1.4:** System shall handle appointment booking conflicts in real-time

#### 3.2.2 Security Requirements
- **NFR-2.1:** All passwords shall be hashed using Django's built-in password hashers
- **NFR-2.2:** System shall implement CSRF protection for all forms
- **NFR-2.3:** System shall use HTTPS for all communications
- **NFR-2.4:** Admin panel shall be protected with role-based access control
- **NFR-2.5:** System shall implement session timeout after 30 minutes of inactivity
- **NFR-2.6:** System shall log all admin actions for audit purposes

#### 3.2.3 Usability Requirements
- **NFR-3.1:** System shall provide bilingual support (English and Urdu)
- **NFR-3.2:** Interface shall be intuitive requiring minimal training
- **NFR-3.3:** System shall be responsive and mobile-friendly
- **NFR-3.4:** Error messages shall be clear and actionable
- **NFR-3.5:** Font sizes shall be readable on mobile devices (minimum 14px)

#### 3.2.4 Reliability Requirements
- **NFR-4.1:** System shall have 99% uptime during business hours
- **NFR-4.2:** System shall perform automatic database backups daily
- **NFR-4.3:** System shall gracefully handle errors without exposing sensitive information
- **NFR-4.4:** System shall maintain data integrity during concurrent operations

#### 3.2.5 Maintainability Requirements
- **NFR-5.1:** Code shall follow Django best practices and PEP 8 style guide
- **NFR-5.2:** System shall have modular architecture for easy updates
- **NFR-5.3:** Database schema shall be managed through Django migrations
- **NFR-5.4:** System shall include comprehensive error logging

#### 3.2.6 Cultural and Regional Requirements
- **NFR-6.1:** System shall use Pakistan Standard Time (PST/PKT)
- **NFR-6.2:** Currency shall be displayed in Pakistani Rupees (PKR)
- **NFR-6.3:** Phone number format shall follow Pakistani standards
- **NFR-6.4:** System shall accommodate women-only service context
- **NFR-6.5:** Content shall be culturally appropriate for local community

---

## 4. External Interface Requirements

### 4.1 User Interfaces

**UI-1: Customer Portal**
- Home page with salon information and featured packages
- Registration and login pages
- Service packages catalog page with filtering options
- Appointment booking page with calendar/time slot selection
- User dashboard showing appointments and profile
- Responsive design for mobile and desktop

**UI-2: Admin Portal**
- Admin login page
- Dashboard with overview statistics
- Appointment management page with calendar view
- Customer list and details page
- Package management page
- Settings page

### 4.2 Hardware Interfaces
- No direct hardware interfaces required
- Standard web server hardware specifications
- Client devices: smartphones, tablets, desktop computers

### 4.3 Software Interfaces

**Database Interface:**
- Django ORM for database operations
- PostgreSQL/SQLite database management system
- Support for database migrations and rollbacks

**Email/SMS Service:**
- Integration with email service (SMTP or third-party like SendGrid)
- Optional SMS gateway integration for Pakistani mobile networks

**External Libraries:**
- Django authentication system
- Django REST Framework (if API needed)
- Frontend libraries (Bootstrap/Tailwind for responsive UI)

### 4.4 Communication Interfaces
- HTTP/HTTPS protocols for web communication
- SMTP for email notifications
- RESTful API standards for potential mobile app integration

---

## 5. System Features

### 5.1 Priority Classification
- **Critical:** User authentication, appointment booking, admin appointment viewing
- **High:** Package display, appointment management, customer dashboard
- **Medium:** Notification system, reporting features
- **Low:** Advanced filtering, analytics dashboard

---

## 6. Database Requirements

### 6.1 Data Models

**User Model:**
- User ID, Name, Email, Phone, Password Hash, User Type (Customer/Admin), Registration Date, Last Login

**Appointment Model:**
- Appointment ID, Customer ID, Service/Package ID, Date, Time, Duration, Status (Pending/Confirmed/Completed/Cancelled), Notes, Created At, Updated At

**Service Package Model:**
- Package ID, Name, Description, Category, Price, Duration, Services Included, Image URL, Active Status, Created At, Updated At

**Booking Slot Model:**
- Slot ID, Date, Start Time, End Time, Is Available, Appointment ID (if booked)

### 6.2 Data Retention
- Customer data: Retained as long as account is active
- Appointment history: Retained for minimum 2 years
- Cancelled appointments: Retained for 1 year
- System logs: Retained for 6 months

---

## 7. Other Requirements

### 7.1 Legal and Compliance
- System shall comply with Pakistan's data protection regulations
- System shall display terms of service and privacy policy
- System shall obtain customer consent for data collection
- System shall provide data export functionality for customers

### 7.2 Business Rules
- Appointments can only be booked during salon working hours
- Minimum advance booking time: 2 hours
- Maximum advance booking time: 60 days
- Cancellation allowed up to 4 hours before appointment
- Salon working hours: 10 AM to 8 PM (configurable by admin)
- Weekly holiday: Configurable (typically Monday for salons in Pakistan)

---

## 8. Appendices

### 8.1 Development Phases

**Phase 1: Core Functionality (4-6 weeks)**
- User authentication system
- Basic appointment booking
- Package display
- Admin appointment viewing

**Phase 2: Enhanced Features (3-4 weeks)**
- Notification system
- Advanced admin features
- Reporting dashboard
- UI/UX refinements

**Phase 3: Testing and Deployment (2-3 weeks)**
- System testing
- User acceptance testing
- Deployment and training
- Documentation

### 8.2 Success Criteria
- System successfully processes appointment bookings
- Admin can manage all appointments effectively
- 90% of test users can complete booking without assistance
- System performs reliably under expected load
- Positive feedback from salon owner and customers

### 8.3 Risks and Mitigation

**Technical Risks:**
- Internet connectivity issues → Implement offline-first PWA capabilities
- Server downtime → Use reliable hosting with backup systems
- Data loss → Automated daily backups

**Business Risks:**
- Low user adoption → Provide training and support
- Technical literacy barriers → Simple, intuitive interface design
- Language barriers → Bilingual interface implementation

---

## 9. Approval

This Software Requirements Specification has been reviewed and approved by:

**Client Representative:**  
Name: _________________  
Signature: _________________  
Date: _________________

**Project Manager:**  
Name: _________________  
Signature: _________________  
Date: _________________

**Lead Developer:**  
Name: _________________  
Signature: _________________  
Date: _________________

---

**Document Control:**
- Version 1.0 - Initial Release
- This document will be updated as requirements evolve during development