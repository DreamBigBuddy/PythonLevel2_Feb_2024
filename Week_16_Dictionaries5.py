# Phonebook Application

contacts = {}

choice = ""

print("Welcome to the phonebook app!")

while choice != "6":
    print('''Please select an option:
1. Add a contact
2. Update a contact
3. Remove a contact
4. View a contact
5. View all contacts
6. Quit''')
 
    choice = input("> ")

    if choice == "1":
        name = input("Enter the name: ")
        phone_number = input("Enter the number: ")

        contacts[name] = phone_number

    elif choice == "2":
        update_choice = input("Change the name or number? ")
        while update_choice != "name" and update_choice != "number":
            print("Try again")
            update_choice = input("Change the name or number? ")

        if update_choice == "name":
            name = input("Enter the name of the contact: ")
            new_name = input("Enter the name for the contact: ")

            phone_number = contacts[name]
            contacts.pop(name)
            contacts[new_name] = phone_number

        elif update_choice == "number":
            name = input("Enter the name of the contact: ")
            phone_number = input("Enter the new number: ")
            contacts[name] = phone_number

    elif choice == "3":
        remove_choice = input("Remove by name or number? ")
        while remove_choice != "name" and remove_choice != "number":
            print("Try again")
            remove_choice = input("Remove by name or number? ")

        if remove_choice == "name":
            name = input("Enter the name of the contact to remove: ")
            contacts.pop(name)

        elif remove_choice == "number":
            number = input("Enter the number of the contact to remove: ")

            for i in contacts:
                if contacts[i] == number:
                    contacts.pop(i)
                    break

    elif choice == "4":
        search_choice = input("Search by name or number? ")
        while search_choice != "name" and search_choice != "number":
            print("Try again")
            search_choice = input("Search by name or number? ")

        if search_choice == "name":
            name = input("Enter the name of the contact to search for: ")
            print(f"Name: {name}, Number: {contacts[name]}")

        elif search_choice == "number":
            number = input("Enter the number of the contact to search for: ")

            for i in contacts:
                if contacts[i] == number:
                    print(f"Name: {i}, Number: {number}")
                    break

    elif choice == "5":
        for i in contacts:
            print(f"Name: {i}, Number: {contacts[i]}")
