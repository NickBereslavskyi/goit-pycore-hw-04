from pprint import pprint

def parse_input(user_input):
    
    # if len(user_input) == 3:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
    

def add_contact(args, contacts):
    name, phone = args
        
    if name in contacts.keys():
        print(f"{name} is already in your contact list, I recommend specifying his first and last name through _ (Bill_Gates)")
        return "Contact not added."
    else:
        contacts[name] = phone
        return "Contact added."
    

def change_username_phone(args, contacts):
    name, phone = args

    if name in contacts.keys():
        agreement = input(f"Are you sure?(Y/N): ")

        if agreement == "Y":
            contacts[name] = phone
            return f"Contact updated. Check: {args}"
            
        else:
            return "Always check twice!"
    else:
        print(f"You specified - {args}, check the input format")
        return "Contact not updated."
    

def show_current_phone_number(name, contacts):
    
    if name in contacts.keys():
        return f"{name}'s phone number is - {contacts[name]}."
    else:
        return f"The name {name} is absent in your contact list"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2: 
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_username_phone(args, contacts))
        elif command == "phone" and args[0] in contacts and len(args) == 1:
            print(show_current_phone_number(args[0], contacts))
        elif command == "all":
            pprint(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()