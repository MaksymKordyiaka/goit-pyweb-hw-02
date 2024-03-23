from collections import UserDict
from datetime import datetime

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Record with name '{name}' not found in the address book.")

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        birthdays = []
        for user in self.data.values():
            if user.birthday:
                birth_date = datetime.strptime(user.birthday.value, '%d.%m.%Y').date().replace(year=today.year)
                difference_date = (birth_date - today).days
                if 0 <= difference_date <= 7:
                    if birth_date.isoweekday() < 6:
                        birthdays.append({'name': user.name.value, 'birthday': birth_date.strftime('%d.%m.%Y')})
                    else:
                        birthdays.append({'name': user.name.value, 'birthday': birth_date.strftime('%d.%m.%Y')})
        return birthdays
