def generate_bene_cust_id():
    bene_cust_id = random.randint(100000, 1000000000)
    return str(bene_cust_id).zfill(10)

def generate_bene_relationship():
    cust_bene_relationship = random.randint(1, 10)
    return cust_bene_relationship

def generate_bene_tax_id():
    area_num = fake.random_number(digits=3, fix_len=True)
    group_num = fake.random_number(digits=2, fix_len=True)
    serial_num = fake.random_number(digits=4, fix_len=True)
    return f"{area_num}-{group_num}-{serial_num}"

def generate_bene_portion(num_beneficiaries):
    return round(100 / num_beneficiaries, 2)
