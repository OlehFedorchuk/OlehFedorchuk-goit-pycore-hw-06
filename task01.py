from collections import UserDict

class Field:
    """
    Base class for fields in a record. Stores a single value.
    """
    def __init__(self, value):
        """
        Initialize the field with a value.
        :param value: The value to store in the field.
        """
        self.value = value

    def __str__(self):
        """
        Return the string representation of the field's value.
        """
        return str(self.value)

class Name(Field):
    """
    Represents the name of a contact. Inherits from Field.
    """
    def __init__(self, value):
        """
        Initialize the name field. Ensures the name is not empty.
        :param value: The name value.
        :raises ValueError: If the name is empty.
        """
        if not value:
            raise ValueError("The name cannot be empty.")
        super().__init__(value)

class Phone(Field):
    """
    Represents a phone number. Inherits from Field.
    """
    def __init__(self, value):
        """
        Initialize the phone field. Ensures the phone number is valid.
        :param value: The phone number value.
        :raises ValueError: If the phone number is not 10 digits.
        """
        if not value.isdigit() or len(value) != 10:
            raise ValueError("The phone number must contain exactly 10 digits")
        super().__init__(value)

class Record:
    """
    Represents a contact record, which includes a name and a list of phone numbers.
    """
    def __init__(self, name):
        """
        Initialize the record with a name.
        :param name: The name of the contact.
        """
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """
        Add a phone number to the record.
        :param phone: The phone number to add.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """
        Remove a phone number from the record.
        :param phone: The phone number to remove.
        :return: True if the phone was removed, False otherwise.
        """
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        """
        Edit an existing phone number in the record.
        :param old_phone: The phone number to replace.
        :param new_phone: The new phone number.
        :return: True if the phone was updated, False otherwise.
        """
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False

    def find_phone(self, phone):
        """
        Find a phone number in the record.
        :param phone: The phone number to find.
        :return: The Phone object if found, None otherwise.
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        """
        Return the string representation of the record.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """
    Represents an address book, which is a collection of records.
    """
    def add_record(self, record):
        """
        Add a record to the address book.
        :param record: The Record object to add.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """
        Find a record by name.
        :param name: The name of the contact to find.
        :return: The Record object if found, None otherwise.
        """
        return self.data.get(name)

    def delete(self, name):
        """
        Delete a record by name.
        :param name: The name of the contact to delete.
        """
        if name in self.data:
            del self.data[name]

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")
book.delete("Jane")
