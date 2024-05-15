# Phonebook Application

contacts = {}

choice = ""

print("Welcome to the phonebook app!")

while choice != "5":
    print('''Please select an option:
1. Add a contact
2. Update a contact
3. Remove a contact
4. Find a contact
5. Quit''')
 
e   choice = input("> ")

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
