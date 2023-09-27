from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)    

class Phone(Field):
    def __init__(self, phone):
        if len(str(phone)) == 10 and str(phone).isdigit():
            super().__init__(phone)
        else:
            raise ValueError("Invalid phone number. It should have 10 digits.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def find_phone(self, phone: str = None):
        if self.phones == []:
            return None

        for i in self.phones:
            if i.value == phone:
                return i
        # return None

    def remove_phone(self, phone: str = None):
        if self.phones == []:
            return None
        
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i) 
        # return None
        
    def edit_phone(self, old_phone, new_phone):
            for i in self.phones:
                if i.value == old_phone:
                    i.value = new_phone
                    return
            raise ValueError
             
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
       self.data[record.name.value] = record

    def find(self, name: str):
        for i in self.data:
            if i == name:
                return self.data[i]
        return None 
    

    def delete(self, name: str):
            result = self.data.pop(name, None)
            return result is not None
    