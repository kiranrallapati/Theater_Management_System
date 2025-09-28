# 🎬 Theater Booking System (Python + MySQL)

This is a simple **Theater Booking Management System** built using **Python** and **MySQL**.  
It allows you to manage movies, shows, customers, and ticket bookings directly from a terminal interface.


## 📌 Features

- Add new movies  
- View all movies  
- Add shows for movies  
- View available shows  
- Book tickets (with seat availability check)  
- View all bookings with customer details  


## 🗂️ Project Structure

Theater-Booking-System/
│
├─ theater_booking.py # Main Python program
├─ database.sql # MySQL database & tables
└─ README.md # Documentation


---

## ⚙️ Prerequisites

- Python 3.8+
- MySQL Workbench
- `mysql-connector-python` module

Install the Python dependency:

pip install mysql-connector-python


## 📌 Notes

- Ensure that movie_id exists before adding a show (foreign key constraint).
- You can delete and re-run database.sql if you want to reset the database.
- MySQL Workbench must be running when you execute the Python script.
