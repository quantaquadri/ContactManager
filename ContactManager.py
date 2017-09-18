class Contact:


    def __init__(self, name, phone_number, gender, email_address, postal_address):

        self.name = name
        self.phone_number = phone_number
        self.gender = gender
        self.email_address = email_address
        self.postal_address = postal_address

    def contact(self):
        return '{} {} {} {} {}'.format(self.name, self.phone_number, self.email_address, self.gender, self.postal_address)


# cont_1 = Contact("andrew", "0503040567", "male", "0703", "rel")

# new_contact = Contact(input("Please enter: Name, Phone Number, Gender, email, Postal Address in that order"))

name = input("Enter your name: ")
phone_number = input("Enter the phone number: ")
gender = input("Enter the gender: ")
email_address = input("enter the email: ")
postal_address = input("ENter your postal address: ")

new_contact = Contact(name, phone_number, gender, email_address, postal_address)

print(new_contact.contact())
# cont_1 = Contact("andrew", 0503040567, "male", 0703)

# print(cont_1.email_address)