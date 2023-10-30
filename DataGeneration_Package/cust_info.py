from faker import Faker
from datetime import datetime, timedelta
import random
import time

random.seed(time.time())
fake = Faker("en_US")
def generate_suffix():
    return fake.suffix() if random.random() < 0.03 else None

def generate_middle():
    return fake.first_name() if random.random() < 0.32 else None

def generate_phone_home():
    area_code = fake.random_number(digits=3, fix_len=True)
    central_office_code = fake.random_number(digits=3, fix_len=True)
    line_number = fake.random_number(digits=4, fix_len=True)
    return f"{area_code}-{central_office_code}-{line_number}"

def generate_phone_business():
    area_code = fake.random_number(digits=3, fix_len=True)
    central_office_code = fake.random_number(digits=3, fix_len=True)
    line_number = fake.random_number(digits=4, fix_len=True)
    return (f"{area_code}-{central_office_code}-{line_number}"
            if random.random() < 0.21 else None)

def generate_email():
    birth_year = birth_date[:4]
    
    domain_name = "@example.com"
    
    first_email = [
        first_name.lower(),
        first_name[0].lower(),
        last_name.lower(),
        last_name[0].lower(),
        fake.safe_color_name().lower(),
        fake.word().lower(),
        fake.building_number(),
        fake.street_suffix().lower(),
    ]

    spacing_email = ["_", ".", ""]
    
    first_choice = random.choice(first_email)
    second_email = random.choice(
        [name for name in first_email if name != first_choice])
    third_email = birth_year
    
    if random.random() < 0.36:
        forth_choice = third_email
    else:
        forth_choice = ""
    
    email = f"{first_choice}{random.choice(spacing_email)}{second_email}{forth_choice}{domain_name}"
    
    return email

def generate_num(probability = 0.96):
    return 1 if random.random() < probability else 0

def generate_employment_status(generated_num):
    return 1 if generated_num == 1 else None

def generate_job(generated_num):
    job = fake.job()
     
    # Split by comma and take the first par
    job = job.split(',')[0]
     
    # Split by "/" and take the first par
    job = job.split('/')[0]
    
    # Capitalize job title
    job = str.title((job))
    
    return job if generated_num == 1 else None

def generate_employer(generated_num):
    if generated_num == 1:
        choices = [
            fake.first_name().title() + " " + fake.company_suffix(),
            fake.last_name().title() + " " + fake.company_suffix(),
            fake.safe_color_name().title() + " " + fake.word().title() + " " +
            fake.company_suffix(),
            fake.safe_color_name().title() + " " + fake.company_suffix(),
            fake.word().title() + " " + fake.safe_color_name().title() + " " +
            fake.company_suffix(),
            fake.word().title() + " " + fake.company_suffix(),
            fake.street_suffix().title() + " " + fake.company_suffix(),
            fake.last_name().title() + " & Sons",
            fake.first_name().title() + " & Sons",
        ]

        sep = ","
        return random.choice(choices)

    else:
        return None

def generate_tax_id(num):
    if num == 1:
        area_num = fake.random_number(digits=3, fix_len=True)
        group_num = fake.random_number(digits=2, fix_len=True)
        serial_num = fake.random_number(digits=4, fix_len=True)
        return f"{area_num}-{group_num}-{serial_num}"
    else:
        return None

def generate_exp_date():
    exp_month = random.randint(1, 12)
    exp_year = random.randint(2023, 2035)
    return f"{exp_month}/{exp_year}"

def generate_id_types():
    return random.randint(1, 5)

generated_cust_id = set()

def generate_secondary_id(num):
    while True:  # Infinite loop to keep generating until a unique number is found.
        if num == 1:
            cust_id = random.randint(100000, 999999999)            

            if cust_id not in generated_cust_id:
                generated_cust_id.add(cust_id)
                #Fill empty digits up to 10
                return cust_id
        else:
            return None

def generate_dates():
    # Start date and end date for cust since date, birthdate, and acct closure date
    start_date = datetime(1970, 1, 1)
    end_date = datetime.today()
    
    # Math to get cust since date
    cust_since_math = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    # Math to get birthdate
    years_to_subtract = random.randint(1, 80)
    birth_date_math = cust_since_math - timedelta(days=years_to_subtract * 365)

    # Math to get acct closure date
    closed_date_math = cust_since_math + timedelta(days=random.randint(0, (end_date - cust_since_math).days))

    # 
    cust_since = cust_since_math.strftime("%Y-%m-%d")
    
    birth_date = birth_date_math.strftime("%Y-%m-%d")
    joint_birth_date = birth_date_math.strftime("%Y-%m-%d")
    
    hire_date = cust_since_math.strftime("%Y-%m-%d")
    emp_birth_date = birth_date_math.strftime("%Y-%m-%d")
    
    if random.random() < 0.45:
        termination_date_math = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    else:
        termination_date_math = None
    
    return cust_since, birth_date, joint_birth_date, closed_date_math, emp_birth_date, hire_date, termination_date_math

# Joint information
def generate_joint_email():
    birth_year = birth_date[:4]
    domain_name = "@example.com"
    first_email = [
        joint_first_name.lower(),
        joint_first_name[0].lower(),
        last_name.lower(),
        last_name[0].lower(),
        fake.safe_color_name().lower(),
        fake.word().lower(),
        fake.building_number(),
        fake.street_suffix().lower(),
    ]

    spacing_email = ["_", ".", ""]
    first_choice = random.choice(first_email)
    second_email = random.choice(
        [name for name in first_email if name != first_choice])
    third_email = birth_year
    if random.random() < 0.36:
        forth_choice = third_email
    else:
        forth_choice = ""
    email = f"{first_choice}{random.choice(spacing_email)}{second_email}{forth_choice}{domain_name}"
    return email
