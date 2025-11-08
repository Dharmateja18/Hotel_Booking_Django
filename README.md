# 🏨 Hotel Booking System (Django)

## 📖 Overview
**Hotel_Booking_Django** is a web-based hotel reservation system built with **Django**.  
It enables users to search for hotels, apply filters, and book rooms online with a smooth, modern interface.  
Bookings are tracked with statuses like **Pending**, **Accepted**, and **Rejected** for easy management.

🔗 **Live Demo:** [https://hotel-booking-django.onrender.com](https://hotel-booking-django.onrender.com)  
📦 **GitHub Repo:** [https://github.com/Dharmateja18/Hotel_Booking_Django](https://github.com/Dharmateja18/Hotel_Booking_Django)

---

## 🧠 Features

### 👤 User Features
- Create an account and log in/out securely.
- Browse all hotels with filtering and sorting.
- Search hotels by name, amenities, or price.
- Book hotels directly (status initially set to “Pending”).
- View all personal bookings on a detailed profile page.
- Responsive and mobile-friendly Bootstrap UI.

### 🛠️ Admin Features
- Add, edit, and delete hotel listings.
- Approve or reject bookings.
- Manage amenities, prices, and availability.

---

## 🧩 Tech Stack

| Category | Technologies Used |
|-----------|-------------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Backend** | Django 3.2 (Python) |
| **Database** | SQLite3 |
| **Hosting** | Render (Free Tier) |
| **Version Control** | Git & GitHub |

---

## 🚀 Deployment

This project is deployed for free on **Render**.

🔗 **Live Link:** [https://hotel-booking-django.onrender.com](https://hotel-booking-django.onrender.com)

---

## ⚙️ Installation & Setup (Run Locally)

To run the project on your local system, follow these steps:

```bash
# Clone this repository
git clone https://github.com/Dharmateja18/Hotel_Booking_Django.git
cd Hotel_Booking_Django

# Create a virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
