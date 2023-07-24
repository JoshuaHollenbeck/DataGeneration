from faker import Faker

fake = Faker()

i = 1
while i < 50:
    print(fake.company_suffix())
    i += 1