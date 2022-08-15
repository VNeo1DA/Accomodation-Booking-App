import sqlite3, sys
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QTableWidgetItem,QMessageBox,QLineEdit
from PyQt5.QtCore import Qt, QDate
from sqlite3 import Error
from booking import *

import person
import accomodation

class MyForm(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #set birthday  DateEdit to today's date (as default - user to change during data entry
        self.ui.dateEditBDay.setDateTime(QtCore.QDateTime.currentDateTime())
        #create bookingSystem object to keep track of bookings
        self.bookingSystem = accomodation.BookingSystem()
        
        #to store booking/customer instances
        self.booking = None
        self.customerDetails = None
        #variable to signal inputs are appropriate to store in Database
        self.inputsCorrect = None
        #Add Subwindows
        self.ui.mdiArea.addSubWindow(self.ui.subwindowLogin)
        self.ui.mdiArea.addSubWindow(self.ui.subwindowCustomerEditor)
        self.ui.mdiArea.addSubWindow(self.ui.subwindowViewBookings)        
        self.ui.mdiArea.setActiveSubWindow(self.ui.mdiArea.subWindowList()[0])

        #WINDOW (1):Login SubWindow SIGNAL & SLOTS
        self.ui.btnLogin.clicked.connect(self.verifyLogin)
        self.ui.btnCancel.clicked.connect(self.clearLoginFields)
        self.ui.showPassCodeBox.stateChanged.connect(self.showPassCode)
        #WINDOW (2):
        self.ui.btnAddBooking.clicked.connect(self.makeReservation)
        self.ui.btnCheckOut.clicked.connect(self.saveRecordToDB)
        self.ui.btn_Cancel.clicked.connect(self.clearBookingFields)
        self.ui.actionCustomer_Editor.triggered.connect(self.makeReserveWindow)
        
        #WINDOW (3):
        self.ui.btnViewReservations.clicked.connect(self.viewBookingList)
        self.ui.actionView_Reservations.triggered.connect(self.viewReservations)
        #File Menu Exit
        self.ui.actionExit.triggered.connect(self.safelyExitApp)
        
        
    def verifyLogin(self):
        userDetails = {}#empty dictionary to store {username:password}
        authenticationOK = False
        userDetails.clear()
        try:
            with open("files/authUsers1.txt", "r") as fStream:
                authenticationOK = True #files storing username/passwords found
                for line in fStream:
                    user_Info = line.split(" ")
                    userName = user_Info[0]
                    passcode = user_Info[1].strip('\n')
                    userDetails[userName]= passcode
    
        except FileNotFoundError:
            QMessageBox.warning(self,"Access Denied","Error retrieving authentication details",
                                QMessageBox.Close,QMessageBox.Close)
            #close application since error states user cannot login, due to an error retrieving 
            #file that stores user/passcodes data 
            self.close()

        if(authenticationOK):
            userName = self.ui.lineEditUserName.text()
            passcode = self.ui.lineEditPasscode.text()
            if(userName,passcode) in userDetails.items():
                QMessageBox.information(self,"Login Successful!", "Login Successful!",
                                        QMessageBox.Ok,QMessageBox.Ok)
                self.ui.lineEditUserName.clear()
                self.ui.lineEditPasscode.clear()
                self.ui.labelOutCome.clear()
                self.ui.mdiArea.activateNextSubWindow()
                
            else:
                QMessageBox.warning(self,"Invalid Credentials","The username or password is incorrect.",
                                    QMessageBox.Close, QMessageBox.Close)
                self.ui.labelOutCome.setText("Ensure to Use Proper Case i.e. UPPER/lower")
    def showPassCode(self, state):
        '''
           If checkBox is enabled, view passcode
           else mask(hide) passcode, so that it cannot be seen.
        '''
        if state == Qt.Checked:
            self.ui.lineEditPasscode.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.lineEditPasscode.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    def makeReserveWindow(self):
        self.ui.mdiArea.setActiveSubWindow(self.ui.mdiArea.subWindowList()[1])

    def viewReservations(self):
        self.ui.mdiArea.setActiveSubWindow(self.ui.mdiArea.subWindowList()[2])

    def clearLoginFields(self):
        self.ui.lineEditUserName.clear()
        self.ui.lineEditPasscode.clear()

    def safelyExitApp(self):
        #inform user of the importance of saving their data before terminating program
        safelyExitApp = QMessageBox()
        exitProgram = True 
        if(exitProgram):
            closingMsg = "Please ensure that you have saved\n"
            closingMsg += "your data to the database, as exiting\n"
            closingMsg += "will result in possible data loss.\n\n"
            closingMsg += "Do you wish to exit this program?\n"
            safelyExitApp = QMessageBox.question(self,"Program Closing",closingMsg,
                            QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if(safelyExitApp==QMessageBox.Yes):
            self.close()            
            
    def verifyUserInput(self):
        ''' verifies valid input from user
            returns string with list of omitted/erroneous data, otherwise empty string
        '''
        #variable to store error messages (if any occur)
        errorMsg = ''
        #var to store dateOfBirth/YearOfBirth, used to verify ageRestriction
        dateOfBirth = self.ui.dateEditBDay.date()
        yearOfBirth = dateOfBirth.year()
        yrBornInStr = str(yearOfBirth)
        #variables for booking date
        dateselected=self.ui.calendar.selectedDate()
        todaysDate = QtCore.QDate.currentDate()

        if len(self.ui.lineEditName.text())==0:
            errorMsg += 'Customer Name\n'
        if len(self.ui.lineEditAddress.text())==0:
            errorMsg += 'Address\n'
        if len(self.ui.lineEditPhone.text())==0:
            errorMsg += 'Phone Number\n'
        if len(self.ui.lineEditEmail.text())==0:
            errorMsg += 'email\n'
        #check dateEdit value, bdate must be 18 yrs & older...
        if(yrBornInStr > '2004'):
            errorMsg += 'Person booking must be 18 years or older\n'
        if(dateselected < todaysDate):
            errorMsg += 'Invalid Booking Date\n'
        if(self.ui.spinBoxNoDays.value() <=0):
            errorMsg += 'Must stay atleast 1 day\n'
                
        return errorMsg

    def getPersonDetails(self):
        name = self.ui.lineEditName.text()
        address = self.ui.lineEditAddress.text()
        contact = self.ui.lineEditPhone.text()
        email = self.ui.lineEditEmail.text()
        bday = self.ui.dateEditBDay.date()
        gender = self.ui.genderBox.itemText(self.ui.genderBox.currentIndex())
        smoking = self.ui.prefSmokingBox.itemText(self.ui.prefSmokingBox.currentIndex())
        bedSize = self.ui.bedSelectBox.itemText(self.ui.bedSelectBox.currentIndex())
        #create Customer Instance, to be used for making a booking
        customer = person.Customer(name, address, contact, email, bday, gender, smoking, bedSize)

        return customer
    
    def makeReservation(self):
        ''' verify user input, append booking to bookingList 
        '''
        inputErrors = self.verifyUserInput()
        if(len(inputErrors)==0):
            #Since there are no user errors inputs
            arrives = self.ui.calendar.selectedDate() #will be converted to String when saved to DataBase
            daysStaying = self.ui.spinBoxNoDays.value()
            departs = arrives.addDays(daysStaying)
            roomType = self.ui.RoomTypeBox.itemText(self.ui.RoomTypeBox.currentIndex())
            self.customerDetails = self.getPersonDetails()

            self.booking = self.bookingSystem.addBooking(arrives, departs, roomType, self.customerDetails)
            if(self.booking != None):
                successText = 'Booking temporarily added!'
                successText+='\nPlease Check Out below to ensure\n'
                successText+= 'booking details are saved to the Booking List Database'
                QMessageBox.information(self,"Customer Reservation Added!",successText ,
                                        QMessageBox.Ok,QMessageBox.Ok)
                self.inputsCorrect = True #signals all inputs were appropriate
            else:
                #logic
                bookingsFullMsg = "Unfortunately All Rooms are fully booked\n"
                bookingsFullMsg +="Advice customer to book on another day"
                QMessageBox.warning(self,"Bookings Full",bookingsFullMsg,
                                   QMessageBox.Close,QMessageBox.Close)
                
        else: #errors were picked up in user inputs
            #call QMessageBox with
            userErrors = 'The following information is missing or incorrect:\n' + inputErrors
            QMessageBox.warning(self,"Booking Error",userErrors,
                                QMessageBox.Close,QMessageBox.Close)
            
    def calculateRoomCost(self):
        chosenRoomType = self.booking.getRoomType()
        numOfDays = self.ui.spinBoxNoDays.value()
        roomPerDay = 0
        if(chosenRoomType=="Ordinary"):
            roomPerDay = 1000
        if(chosenRoomType=="Super Deluxe"):
            roomPerDay = 1200
        if(chosenRoomType=="Super Luxury"):
            roomPerDay = 1300
        if(chosenRoomType=="Suite"):
            roomPerDay = 1500
        totalCost = numOfDays * roomPerDay

        return totalCost
            
    def saveRecordToDB(self):        
        if(self.inputsCorrect==True):
            arrives = self.booking.getArrival().toString("dd-MM-yyyy")
            departs = self.booking.getDeparture().toString("dd-MM-yyyy")
            roomType = self.booking.getRoomType()         
            name = self.customerDetails.getName()
            address = self.customerDetails.getAddress()
            contact = self.customerDetails.getPhone()
            email = self.customerDetails.getEmail()
            bday = self.customerDetails.getBDay().toString("dd-MM-yyyy")
            gender = self.customerDetails.getGender()
            smoking = self.customerDetails.getSmoking()
            bedSize = self.customerDetails.getBedSize()
            #calculate room Cost(with helper function), and store in totalBill variable
            totalBill = str(self.calculateRoomCost())
            sqlStatement = "INSERT INTO bookingList VALUES (null,'"  + arrives + "','"  + departs + "','" + roomType + "','" + name + "','" + address + "','" + contact + "','" + email + "','" + bday + "','" + gender + "','" + smoking + "','" + bedSize + "'," + (totalBill) + ")"
            print(sqlStatement)
            try:
                conn = sqlite3.connect("Bookings.db")
                with conn:
                    cur = conn.cursor()
                    cur.execute(sqlStatement)
                    conn.commit()
                    successText = "Booking Details have successfully been saved\n"
                    successText += "to the Booking List Database"
                    QMessageBox.information(self,"Booking Added To Database",successText, 
                                    QMessageBox.Ok,QMessageBox.Ok)
                    self.bookingSystem.addToList(self.booking) #append Booking to Booking System's booking list
                    
            except Error as e:
                errorMsg = "Error connecting to the Bookings Database\n"
                errorMsg += "Error could have occured due to the following reasons:\n"
                errorMsg += "- Inaccurate SQL statement(s)\n"
                errorMsg += "- Incorrect database or table name"
                QMessageBox.warning(self,"Database Connection Error",errorMsg,
                                    QMessageBox.Close,QMessageBox.Close)
                conn.rollback()
            
            finally:
                conn.close()

    def clearBookingFields(self):
        self.ui.lineEditName.clear()
        self.ui.lineEditAddress.clear()
        self.ui.lineEditPhone.clear()
        self.ui.lineEditEmail.clear()
        self.ui.dateEditBDay.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.calendar.setSelectedDate(QDate.currentDate())
        
                
    def viewBookingList(self):
        sqlStatement = "SELECT * FROM bookingList"
        try:
            conn = sqlite3.connect("Bookings.db")
            cur = conn.cursor()
            cur.execute(sqlStatement)
            rows = cur.fetchall()
            rowNo=0
            for tup in rows:
                colNo=0               
                for columns in tup:
                    self.ui.tableReserved.setItem(rowNo, colNo, QTableWidgetItem(str(columns)))
                    colNo+=1
                rowNo+=1
            cols = ['Booking Num','Arrival', 'Departure', 'Room Type', 'Name', 'Address','Contact' ,
                    'e-mail', 'Birth-Date','Gender','Smoking','Bed Size', 'Cost']
            self.ui.tableReserved.setHorizontalHeaderLabels(cols)
            self.ui.tableReserved.resizeColumnsToContents()
        except Error as e:
            self.ui.tableReserved.clear()
            QMessageBox.warning(self,"Database Connection Error","Error connecting to the Bookings Database",
                                QMessageBox.Close,QMessageBox.Close)

        finally:
            conn.close()
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

    
