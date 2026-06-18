contacts = { }
def add_contact():
    name = input("enter your name : ")
    phone = input("enter phone number : ")

    contacts[name]=phone
    print("contact added successfully")

def find_contact():
    name = input("search your name ")
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("contact not found")
    
def list_contacts():
    if len(contacts) == 0:
        print("no contacts found")
    else:
        for name , phone  in contacts.items():
          print(f"{name} : {phone}")

def main():
    while True:
        print("\n1. Add Contact")
        print("2. Find Contact")
        print("3. List Contacts")
        print("4. Exit")

        choice = int(input("enter choice : "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            find_contact()
        elif choice == 3:
            list_contacts()
        elif choice == 4:
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()