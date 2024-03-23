from addressbook import AddressBook
from record import Record
import pickle

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError, AttributeError) as error:
            if isinstance(error, ValueError):
                return 'Error! if you want to:\n' \
                       'add contact: you must input ("add" username phone).\n' \
                       'change phone: you must input ("change" username old_phone new_phone) or no contacts.\n' \
                       'get phone: you must input ("phone" username)\n'\
                       'add-birthday: you must input("add-birthday" username DD.MM.YYYY)\n'\
                       'show-birthday: you must input("show-birthday" username)\n'
            elif isinstance(error, AttributeError):
                return 'Atribute error'
            elif isinstance(error, KeyError):
                return 'Key error'
            elif isinstance(error, IndexError):
                return 'Index error'
    return inner

@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return f"Phone number for '{name}' changed."
    else:
        return f"Contact {name} not found."

def show_all(book: AddressBook):
    if not book:
        return 'No contacts available, you need to (add "username" "phone")'
    else:
        result = ''
        for name, phone in book.items():
            result += f"{name}: {phone}\n"
        return result.strip()

@input_error
def get_phone(args, book: AddressBook):
    name, = args
    record = book.find(name)
    if record:
        return f"Phone number for '{name}': {', '.join(str(phone) for phone in record.phones)}"
    else:
        return f"Contact {name} not found."

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for '{name}'."
    else:
        return f"Contact '{name}' not found."

@input_error
def show_birthday(args, book: AddressBook):
    name, = args
    record = book.find(name)
    if record:
        if record.birthday:
            return f"Birthday for '{name}': {record.birthday}"
        else:
            return f"No birthday found for '{name}'. Please add a birthday using 'add-birthday' command."
    else:
        return f"No contact found for '{name}'."

def birthdays(book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays"
    else:
        return "\n".join(f"Upcoming birthday next week for '{b['name']}': {b['birthday']}" for b in upcoming_birthdays)

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_phone(args, book))
        elif command == "phone":
            print(get_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")
    save_data(book)

if __name__ == '__main__':
    main()