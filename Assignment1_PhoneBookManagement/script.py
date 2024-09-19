from contact import Contact
from phonebook import PhoneBook
from inputvalidation import get_validated_input, validate_phone, validate_email

'''
Main function to run the phone book application
Run This File to start the phone book application
'''

def main():
    phone_book = PhoneBook()
    
    while True:
        print("\nPhone book menu(Please select a number):")
        print("1. Add contacts")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Update contacts")
        print("5. Delete contacts")
        print("6. View contact change history")
        print("7. Import contacts from a CSV file")
        print("8. Export contacts to a CSV file")
        print("9. Exit")

        choice = input("Enter a number:")

        #Add contacts
        if choice == '1':
            firstName = input("Enter first name:")
            lastName = input("Enter last name:")
            phone = get_validated_input("Enter phone number (###)###-####:", validate_phone, "Invalid phone format.")
            email = input("Enter email(Optional): ")
            if email:
                email = get_validated_input("Enter email(Optional): ", validate_email, "Invalid email format.")
            else: 
                email = "N/A"
            address = input("Enter address(Optional): ")
            if not address:
                address = "N/A"
            contact = Contact(firstName, lastName, phone, email, address)
            phone_book.add(contact)

        #View Contacts(Grouped by first letter of last name)
        elif choice == '2':
            phone_book.view()
        
        #Search Contacts
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            wildcard = input("Use wildcard search? (y/n): ").lower() == 'y'
            added_since_days = input("Filter contacts added within how many days (leave blank for no filter)?: ")
            added_since_days = int(added_since_days) if added_since_days else None
            results = phone_book.search_contacts(query, wildcard, added_since_days)
            if results:
                for contact in results:
                    print(contact)
            else:
                print("No contacts found")
        
        #Update Contacts
        elif choice == '4':
            fName = input("Enter first name of contact to update:")
            lName = input("Enter last name of contact to update:")
            print("Enter new details (leave blank to keep current value):")
            new_firstName = input("Enter new first name:")
            new_lastName = input("Enter new last name:")
            phone = get_validated_input("Enter new phone number (###)###-####:", validate_phone, "Invalid phone format.")
            email = input("Enter new email(Optional): ")
            if email:
                email = get_validated_input("Enter new email(Optional): ", validate_email, "Invalid email format.")
            address = input("Enter new address(Optional): ")
            # Build the kwargs dictionary only with non-empty values
            kwargs = {}
            if new_firstName:
                kwargs['firstName'] = new_firstName
            if new_lastName:
                kwargs['lastName'] = new_lastName
            if phone:
                kwargs['phone'] = phone
            if email:
                kwargs['email'] = email
            if address:
                kwargs['address'] = address
            phone_book.update(fName, lName, **kwargs)

        #Delete Contacts
        elif choice == '5':
            firstName = input("Enter first name of contact to delete:")
            lastName = input("Enter last name of contact to delete:")
            phone_book.delete(firstName, lastName)

        #View Contact Change History
        elif choice == '6':
            firstName = input("Enter first name of contact to view change history:")
            lastName = input("Enter last name of contact to view change history:")
            phone_book.view_contact_history(firstName, lastName)

        #Import Contacts from a CSV file
        elif choice == '7':
            csv_file = input("Enter CSV file path to import contacts: ")
            phone_book.importFile(csv_file)

        #Export Contacts to a CSV file
        elif choice == '8':
            csv_file = input("Enter CSV file path to export contacts: ")
            phone_book.exportFile(csv_file)

        #Exit
        elif choice == '9':
            break

if __name__ == '__main__':
    main()
