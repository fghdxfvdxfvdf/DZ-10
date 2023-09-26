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
        try:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
        except ValueError as e:
            print(e)

    def find_phone(self, phone):
        result = list(filter(lambda x: x.value == phone, self.phones))
        return result[0] if len(result) > 0 else None

    def remove_phone(self, phone):
        result = list(filter(lambda x: x.value == phone, self.phones))
        if len(result) > 0:
            self.phones.remove(result[0])
            return True
        else:
            return False

    def edit_phone(self, old_phone, new_phone):
        result = list(filter(lambda x: x.value == old_phone, self.phones))
        if len(result) > 0:
            result[0].value = new_phone
            return new_phone
        else:
            raise ValueError("Phone number not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.phones = []

    def add_record(self, record):
       self.data[record.name.value] = record

    def find(self, name):
        result = list(filter(lambda x: x.name.value == name, self.data.values()))
        return result[0] if len(result) > 0 else None

    def delete(self, name):
            result = self.data.pop(name, None)
            return result is not None