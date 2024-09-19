from datetime import datetime

class Contact:
    def __init__(self, firstName, lastName, phone, email=None, address=None):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.email = email
        self.address = address
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.change_history = []

    def update_contact(self, firstName=None, lastName=None, phone=None, email=None, address=None):
        # Capture the old data before updating
        old_data = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
        }

        # Update contact details
        if firstName: self.firstName = firstName
        if lastName: self.lastName = lastName
        if phone: self.phone = phone
        if email: self.email = email
        if address: self.address = address
        self.updated_at = datetime.now()

        # Record the change in history
        new_data = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
        }
        
        # Append to change history only if something was actually updated
        if old_data != new_data:
            self.change_history.append({
                "updated_at": self.updated_at,
                "old": old_data,
                "new": new_data
            })

    def view_change_history(self):
        if not self.change_history:
            print("No changes have been made to this contact.")
            return
        
        for change in self.change_history:
            print(f"Change made on {change['updated_at']}:")
            print(f"Old data: {change['old']}")
            print(f"New data: {change['new']}")

    def __str__(self):
        return f'Name:{self.firstName} {self.lastName} Phone:{self.phone} Email:{self.email} Address:{self.address}'