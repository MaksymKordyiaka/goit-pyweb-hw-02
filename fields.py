from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        try:
            if not value.isdigit() or len(value) != 10:
                raise ValueError("Phone number must contain 10 digits")
            super().__init__(value)
        except AttributeError:
            raise AttributeError('Invalid format number. Use 10 digits')

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        except TypeError:
            raise TypeError("Invalid date format. Use DD.MM.YYYY")