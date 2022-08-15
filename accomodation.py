class Booking:
    def __init__(self, arrivalDate,departureDate,roomType, customer):
        self._arrive = arrivalDate
        self._departureDate = departureDate
        self._roomType = roomType
        self._customer = customer
    #accessor methods
    def getArrival(self):
        return self._arrive

    def getDeparture(self):
        return self._departureDate

    def getRoomType(self):
        return self._roomType
    
    def booked(self,dateOfBooking):
        return(dateOfBooking >= self._arrive and dateOfBooking < self._departureDate)
              
    def __str__(self):

        lines = []
        arrivDate = self._arrive.toString("dd-MM-yyyy")
        departDate = self._departureDate.toString("dd-MM-yyyy")
        lines.append('Arrival date: {}\nDays staying: {}\nRoom type: {}\n'.format(arrivDate, departDate,self._roomType))
        return ''.join(lines)


class BookingSystem:
    #static variable to hold the maximum number of rooms for a single day
    maxRooms = 10

    bookingList = [] #static list, to hold Booking instances

    def roomsAvailable(self, dateBooked):
        '''method to check if rooms are available, it traverses the static variable
        bookingList to check throughout the booked days whether there is a vacancy'''
        numOfRooms = BookingSystem.maxRooms
        for booking in BookingSystem.bookingList:
            if (booking.booked(dateBooked)):
                numOfRooms = numOfRooms - 1
        return numOfRooms
        
    def vacancy(self, arrive, depart):
        if(arrive.isValid() and depart.isValid() and arrive < depart):
            verificationDate = arrive
            while(verificationDate < depart):
                if(self.roomsAvailable(verificationDate) <= 0):
                    return False
                verificationDate = verificationDate.addDays(1)
            return True
        else:
            return False

           
    def addBooking(self, arrival, depart,roomType, customer):
        booking = None
        if(self.vacancy(arrival,depart)==True):
            #if there are rooms available create the booking
            booking = Booking(arrival, depart, roomType, customer)

        #we return booking reference if rooms available, if it happens to be NONE; inform user that NO VACANCY AVAILABLE
        return booking

    def addToList(self, booking):
        BookingSystem.bookingList.append(booking)
        print(len(BookingSystem.bookingList))
        
