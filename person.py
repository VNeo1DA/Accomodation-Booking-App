class Customer:
    def __init__(self,name, address,phone,email,birthdate,gender,smoking,bed):
        self._name = name
        self._address = address
        self._phone = phone
        self._email = email
        self._bday = birthdate
        self._gender = gender
        self._smoking = smoking
        self._bed = bed

    def getName(self):
        return self._name
    def getAddress(self):
        return self._address
    def getPhone(self):
        return self._phone
    def getEmail(self):
        return self._email
    def getBDay(self):
        return self._bday
    def getGender(self):
        return self._gender
    def getSmoking(self):
        return self._smoking
    def getBedSize(self):
        return self._bed
    
    def __str__(self):
        lines=[]
        #verification method to ensure all LineEdits & choiceBox input received
        birthDate = self._bday.toString("dd-MM-yyyy")
        lines.append('{}, {}, {}, {}, {}, {}, {}, {}'.format(self._name,self._address, self._phone, self._email,
                                                   birthDate, self._gender, self._smoking,self._bed))
        return''.join(lines)
