def generate_emp_suffix():
    return fake.suffix() if random.random() < 0.03 else None

def generate_middle():
    return fake.first_name() if random.random() < 0.32 else None

def generate_emp_phone():
    area_code = fake.random_number(digits=3, fix_len=True)
    central_office_code = fake.random_number(digits=3, fix_len=True)
    line_number = fake.random_number(digits=4, fix_len=True)
    return f"{area_code}-{central_office_code}-{line_number}"

def generate_emp_tax_id():
    area_num = fake.random_number(digits=3, fix_len=True)
    group_num = fake.random_number(digits=2, fix_len=True)
    serial_num = fake.random_number(digits=4, fix_len=True)
    return f"{area_num}-{group_num}-{serial_num}"

def get_termination_reason(termination_date_math):
    if termination_date_math is None:
        return None
    else:
        return random.randint(1, 4)

def get_rehireable(termination_reason_result):
    if termination_reason_result in [1, 2, 3]:
        return 1
    elif termination_reason_result == 4:
        return 0

def generate_emp_pass():
    if main_client == 1:
        emp_pass = fake.password(length=8)
        return emp_pass
    else:
        return None
