from fields import Name, Phone, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, b_day):
        self.birthday = Birthday(b_day)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = self.find_phone(old_phone)
        if old_phone_obj:
            if not new_phone.isdigit() or len(new_phone) != 10:
                raise ValueError("New phone number must contain 10 digits")
            old_phone_obj.value = new_phone
        else:
            raise ValueError("Phone number not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {str(self.name)}, phone: {'; '.join(str(p) for p in self.phones)}, birthdate: {self.birthday}"
