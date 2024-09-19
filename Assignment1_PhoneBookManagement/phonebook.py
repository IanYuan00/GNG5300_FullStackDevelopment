from contact import Contact
from datetime import datetime, timedelta
import re
import csv

class PhoneBook:
    def __init__(self):
        self.contacts = []
    
    # Add a new contact
    def add(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
            self.log_operation(f'Add contact: Name: {contact.firstName} {contact.lastName}; Phone Number: {contact.phone}; Email: {contact.email}; Address: {contact.address}.')
            print(f'Contact added: Name: {contact.firstName} {contact.lastName}; Phone Number: {contact.phone}; Email: {contact.email}; Address: {contact.address}.')
        else:
            print("Contact already exists")

    # View all contacts grouped by first letter of last name
    def view(self):
        if self.contacts:
            # Group contacts by first letter of last name
            grouped_contacts = {}
            for contact in self.contacts:
                first_letter = contact.lastName[0].upper()  # Get the first letter of the last name
                if first_letter not in grouped_contacts:
                    grouped_contacts[first_letter] = []
                grouped_contacts[first_letter].append(contact)
    
            for letter, contacts in grouped_contacts.items():
                print(f"\nContacts starting with '{letter}':")
                for contact in contacts:
                    print(contact)
            self.log_operation(f'Viewed all contacts')
        else:
            print("Contact not found")

    # Search contacts by name or phone number
    def search_contacts(self, query=None, wildcard=False, added_since_days=None):
        results = self.contacts

        #Wildcard search
        if query:
            if wildcard:
                pattern = re.compile(query.replace('*', '.*'))
            else:
                pattern = re.compile(re.escape(query), re.IGNORECASE)
            results = [contact for contact in results if pattern.search(contact.firstName) or pattern.search(contact.lastName) or pattern.search(contact.phone)]

        #Filter by days since added
        if added_since_days:
            time_threshold = datetime.now() - timedelta(days = added_since_days)
            results = [contact for contact in results if contact.created_at >= time_threshold]

        self.log_operation(f'Searched contacts with query: {query} wildcard: {wildcard} added_since_days: {added_since_days}')

        return results

    # Update contact details
    def update(self, firstName, lastName, **kwargs):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                contact.update_contact(**kwargs)
                print(f"Contact updated: Name:{contact.firstName} {contact.lastName}; Phone Number:{contact.phone}; Email:{contact.email}; Address:{contact.address}.")
                self.log_operation(f'updated contact: Name:{contact.firstName} {contact.lastName}; Phone Number:{contact.phone}; Email:{contact.email}; Address:{contact.address}.')
                return
        print("Contact not found.")

    # Delete a contact
    def delete(self, firstName, lastName):
        for contact in self.contacts:
            if contact.firstName ==firstName and contact.lastName == lastName:
                self.contacts.remove(contact)
                self.log_operation(f'Deleted contact: Name:{contact.firstName} {contact.lastName}; Phone Number:{contact.phone}; Email:{contact.email}; Address:{contact.address}')
                print(f"Deleted contact: Name:{contact.firstName} {contact.lastName}; Phone Number:{contact.phone}; Email:{contact.email}; Address:{contact.address}")
                return
        print("Contact not found")

    # View contact change history
    def view_contact_history(self, firstName, lastName):
        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                contact.view_change_history()
                self.log_operation(f'Viewed Contact Change History: Name:{contact.firstName} {contact.lastName}; Phone Number:{contact.phone}; Email:{contact.email}; Address:{contact.address}')
                return
        print("Contact not found")

    # Import contacts from a CSV file
    def importFile(self, csv_file):
        try:
            with open(csv_file, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 3:
                        contact = Contact(
                            firstName = row[0],
                            lastName = row[1],
                            phone = row[2],
                            email = row[3] if len(row) >= 4 else None,
                            address = row[4] if len(row) >= 5 else None
                        )
                        self.add(contact)
        except Exception as e:
            print("Error importing from CSV: {e}")

    # Export contacts to a CSV file
    def exportFile(self, csv_file):
        try:
            with open(csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                for contact in self.contacts:
                    writer.writerow([contact.firstName, contact.lastName, contact.phone, contact.email, contact.address])
        except Exception as e:
            print(f"Error exporting to CSV: {e}")

    # Log operations
    def log_operation(self, operation):
        with open('./activity.log', 'a') as f:
            f.write(f'{datetime.now()} - {operation}\n')
