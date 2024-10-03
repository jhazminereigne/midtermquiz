import requests
import json
from faker import Faker

fake=Faker()
for i in range(1,11):
    fakename= fake.name()
    fakeemail= fake.email()
    fakenum =fake.phone_number()
    print("Name: ", fakename, "Email: " , fakeemail, "Phone Number: ",fakenum )