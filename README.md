# Accomodation-Booking-App
Guest-House-Booking-System
This is a Python Desktop Graphical User Interface (GUI) application that simulates an accomodation booking sub-system. It consists of a three sub windows (i) a Login subwindow, (ii) Customer Reservation subwindow and (iii) View Reservation subwindow.
It uses a Composition Design Pattern, whereby a Person module(representing the customer) is loosely coupled with the Booking module, and the Booking module (representing the booking made by a customer) has a relationship with the Booking System (both in accomodation module).
The Application uses mechanisms to limit the number of rooms available on a given date, and only when there is a vacancy can the bookings be successfully added and stored in the database Bookings.db

Application uses a minimalistic design (User Interface) designed with QtDesigner, coded with PyQt5 / python 3+
In order to run the application
please install:
(1) PyQt5
(2) python 3.4 or above
the applications are free/open source (including QtDesigner and can be downloaded for free)
(3) Database Management System Used: DB Browser for SQLite 3.12 or above 

visit for installation files:
https://sourceforge.net/
https://sqlitebrowser.org/
