# def populate_data(num):
#     for i in range(num):
#         person = Person()
#         person.name = fake.name()
#         person.id = fake.random_int()
#         person.contact = fake.phone_number()
#         person.address = fake.address()
#         person.save()

# populate_data(30)

from django.db import models
from faker import Faker
from .models import Name, ID, Contact, Address

def populate_data():
    fake = Faker()
    for _ in range(30):
        name = Name(name=fake.name())
        name.save()
        id_number = ID(id_number=fake.random_int())
        id_number.save()
        contact = Contact(email=fake.email(), phone_number=fake.phone_number())
        contact.save()
        address = Address(address_line1=fake.address(), city=fake.city(), state=fake.state(), zip_code=fake.zipcode())
        address.save()
    return {"response": "data added"}
