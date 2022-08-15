import person
from PyQt5 import QtCore
import accomodation

#in this application we will test booking system cls

#main
#1 create person Object
toDay = QtCore.QDate.currentDate()
cust1 = person.Customer('Jane', '45 Fox Str, Pretoria', '079067','jane@email.net',
                        toDay,'female','No','King')
departDate = toDay.addDays(2)
roomType = 'Super Deluxe'
#test the booking System, if it works

#DB list
bookedList = []
bookings = accomodation.BookingSystem()

ref1 = bookings.addBooking(toDay, departDate, roomType, cust1)
count = 0
if(ref1 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref1)
    print("Booking Number ", count, " added, details are:")
    print(ref1)


cust2 = person.Customer('John', '5 Milton Ave, Rivonia', '073068','john@ymail.net',
                        toDay,'Male','Yes','Quarter')
departDate2 = toDay.addDays(2)
roomType2 = 'Deluxe'

ref2 = bookings.addBooking(toDay, departDate2, roomType2, cust2)
if(ref2 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref2)
    print("Booking Number ", count, " added, details are:")
    print(ref2)

cust3 = person.Customer('Conor', '2 Plain Ave, Sandown', '067062','conor@xmail.net',
                        toDay,'Male','Yes','King')
departDate3 = toDay.addDays(2)
roomType3 = 'Ordinary'
ref3 = bookings.addBooking(toDay, departDate3, roomType3, cust3)
if(ref3 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref3)
    print("Booking Number ", count, " added, details are:")
    print(ref3)

cust4 = person.Customer('Matilda', '56 West Str, Polokwane', '066991','matilda@ymail.net',
                        toDay,'Female','Yes','Single')
departDate4 = toDay.addDays(2)
roomType4 = 'Suite'
ref4 = bookings.addBooking(toDay, departDate4, roomType4, cust4)
if(ref4 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref4)
    print("Booking Number ", count, " added, details are:")
    print(ref4)

cust5 = person.Customer('Sarah', '2 Sunset Str, Soweto', '076921','sarah@ymail.net',
                        toDay,'Female','Yes','Three Quarter')
departDate5 = toDay.addDays(2)
roomType5 = 'Super Luxury'
ref5 = bookings.addBooking(toDay, departDate5, roomType5, cust5)
if(ref5 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref5)
    print("Booking Number ", count, " added, details are:")
    print(ref5)

cust6 = person.Customer('Nash', '1 Benton Rd, Polokwane', '061134','nash@gmail.net',
                        toDay,'Male','No','King')
departDate6 = toDay.addDays(2)
roomType6 = 'Ordinary'
ref6 = bookings.addBooking(toDay, departDate6, roomType6, cust6)
if(ref6 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref6)
    print("Booking Number ", count, " added, details are:")
    print(ref6)

cust7 = person.Customer('Jenny', '12 Milk Ave, Pretoria', '082124','jenny@hotmail.net',
                        toDay,'Female','No','Queen')
departDate7 = toDay.addDays(2)
roomType7 = 'Suite'
ref7 = bookings.addBooking(toDay, departDate7, roomType7, cust7)
if(ref7 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref7)
    print("Booking Number ", count, " added, details are:")
    print(ref7)

cust8 = person.Customer('Timothy', '22 Smith Ave, Cape-Town', '063402','tim@hotmail.net',
                        toDay,'Male','No','Three Quarter')
departDate8 = toDay.addDays(2)
roomType8 = 'Super Luxury'
ref8 = bookings.addBooking(toDay, departDate8, roomType8, cust8)
if(ref8 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref8)
    print("Booking Number ", count, " added, details are:")
    print(ref8)

cust9 = person.Customer('Gilda', '87 Thabo Mbeki Drive, Pretoria', '073403','gilda3@ymail.net',
                        toDay,'Female','Yes','Single')
departDate9 = toDay.addDays(2)
roomType9 = 'Ordinary'
ref9 = bookings.addBooking(toDay, departDate9, roomType9, cust9)
if(ref9 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref9)
    print("Booking Number ", count, " added, details are:")
    print(ref9)

cust10 = person.Customer('Christof', '4 Nelson Mandela Ave, Pretoria', '083302','chris@gmail.net',
                        toDay,'Male','Yes','King')
departDate10 = toDay.addDays(2)
roomType10 = 'Super Deluxe'
ref10 = bookings.addBooking(toDay, departDate9, roomType9, cust9)
if(ref10 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref10)
    print("Booking Number ", count, " added, details are:")
    print(ref10)
#breakPoint
cust11 = person.Customer('Ricky', '3 Westbeach Str, Durban', '079332','rick@hotmail.net',
                        toDay,'Male','Yes','Queen')
departDate11 = toDay.addDays(2)
roomType11 = 'Suite'
ref11 = bookings.addBooking(toDay, departDate9, roomType9, cust9)
if(ref11 == None):
    print("Booking Failed")
else:
    count = count + 1
    bookings.addToList(ref11)
    print("Booking Number ", count, " added, details are:")
    print(ref11)
