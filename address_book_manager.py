# Function to add a new contact
# def add_contact(address_book, name, phone):
#     address_book[name] = phone
#     print(f"Contact '{name}' added successfully!")

# # Function to search for a contact
# def search_contact(address_book, name):
#     if name in address_book:
#         print(f"Contact Found - Name: {name}, Phone: {address_book[name]}")
#     else:
#         print(f"Contact '{name}' not found.")

# # Function to update a contact's phone number
# def update_contact(address_book, name, new_phone):
#     if name in address_book:
#         address_book[name] = new_phone
#         print(f"Contact '{name}' updated successfully!")
#     else:
#         print(f"Contact '{name}' not found.")

# # Function to delete a contact
# def delete_contact(address_book, name):
#     if name in address_book:
#         del address_book[name]
#         print(f"Contact '{name}' deleted successfully!")
#     else:
#         print(f"Contact '{name}' not found.")

# # Main function to run the address book manager
# def main():
#     address_book = {}  # Empty dictionary to store contacts

#     while True:
#         print("\nAddress Book Manager")
#         print("1. Add Contact")
#         print("2. Search Contact")
#         print("3. Update Contact")
#         print("4. Delete Contact")
#         print("5. Exit")

#         choice = input("Enter your choice (1-5): ")

#         if choice == '1':
#             name = input("Enter contact name: ")
#             phone = input("Enter contact phone number: ")
#             add_contact(address_book, name, phone)
#         elif choice == '2':
#             name = input("Enter contact name to search: ")
#             search_contact(address_book, name)
#         elif choice == '3':
#             name = input("Enter contact name to update: ")
#             new_phone = input("Enter new phone number: ")
#             update_contact(address_book, name, new_phone)
#         elif choice == '4':
#             name = input("Enter contact name to delete: ")
#             delete_contact(address_book, name)
#         elif choice == '5':
#             print("Exiting Address Book Manager. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
# main()


# Mine Code:


def main():
    dic = {}

    while True:
        print("\nAddress Book Manager")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = int(input("Please enter your choice number "))

        if (choice == 1):
            contactName = input("Please enter contact name ")
            contactNumber = input("Please enter contact number ")
            addContact(dic, contactName, contactNumber)
        elif (choice == 2):
            contactName = input("Please enter contact name to search ")
            searchContact(dic, contactName)
        elif (choice == 3):
            contactName = input("Please enter contact name to update ")
            contactNumber = input("Please enter new number ")
            updateContact(dic, contactName, contactNumber)
        elif (choice == 4):
            contactName = input("Please enter contact name to delete ")
            delContact(dic, contactName)
        elif (choice == 5):
            break
        else:
            print("Invalid choice")


def addContact(dic: dict, name: str, number: int):
    dic.update({name: number})
    print(f"Successfully added {name} = {number}")


def searchContact(dic: dict, name: str) -> None:
    print(name in dic)

    if name in dic:
        contact = dic.get(name)
        print(f"\nYou Contact found :  {name} = {contact}\n")
    else:
        print(f"\nNot found {name}\n")


def updateContact(dic: dict, name: str, number: int):
    if name in dic:
        dic[name] = number
        print("Updated successfully")
    else:
        print("Not found")


def delContact(dic: dict, name: str):
    if name in dic:
        del dic[name]
        print("Successfully deleted")
    else:
        print("Not found")


main()
