contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found. Please enter a valid name."
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "Insufficient arguments. Please provide both name and phone."
    return inner

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added"

@input_error
def change_contact(args):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated, new phone {phone}."
    else:
        raise KeyError

@input_error
def get_phone(args):
    name = args[0]
    if name in contacts:
        return f"{contacts[name]}."
    else:
        raise KeyError

@input_error
def show_all(_):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."

def main():
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": show_all,
    }

    while True:
        user_input = input("Enter command: ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        handler = commands.get(command)
        
        if handler:
            print(handler(args))
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
