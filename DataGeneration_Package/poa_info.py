def generate_poa_chance():
    if random.random() < 0.15:
        poa_num = 1
    else:
        poa_num = 0
    
    return poa_num

def generate_poa_role(poa_num):
    if poa_num == 1:
        cust_poa = random.randint(1, 3)
        return cust_poa
    else:
        return None

def generate_poa_first_name(poa_num):
    if poa_num == 1:
        return fake.first_name()
    else:
        return None

def generate_poa_last_name(poa_num):
    if poa_num == 1:
        return fake.last_name()
    else:
        return None
