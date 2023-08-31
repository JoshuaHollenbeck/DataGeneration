from tqdm import tqdm
from faker import Faker
from datetime import datetime, timedelta
from _city_info import *
import random
import string
import pandas as pd
import copy

fake = Faker("en_US")

# Customer information


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


def generate_employment(generated_num):
    return 1 if generated_num == 1 else None


def generate_job(generated_num):
    return fake.job() if generated_num == 1 else None


def generate_employer(generated_num):
    return employer_choice if generated_num == 1 else None


def generate_ssn_front():
    area_num = fake.random_number(digits=3, fix_len=True)
    group_num = fake.random_number(digits=2, fix_len=True)
    return f"{area_num}-{group_num}"


def generate_ssn_back():
    serial_num = fake.random_number(digits=4, fix_len=True)
    return serial_num


def generate_exp_date():
    exp_month = random.randint(1, 12)
    exp_year = random.randint(2023, 2035)
    return f"{exp_month}/{exp_year}"


def generate_id_type():
    return random.randint(1, 5)


def generate_is_organization():
    return "0"

# Joint information


def generate_joint_employment(generated_joint_num):
    return 1 if generated_joint_num == 1 else None


def generate_joint_job(generated_joint_num):
    return fake.job() if generated_joint_num == 1 else None


def generate_joint_employer(generated_joint_num):
    return employer_choice if generated_joint_num == 1 else None

# Account information


def generate_contact_method():
    return 1 if random.random() < 0.34 else None


def generate_acct_num():
    return random.randint(10000000, 99999999)


def generate_initial_contact_method():
    initial_contact = ["1", "2", "3", "4"]
    return random.choice(initial_contact)


def generate_investment_objectives():
    client_investment_objective = random.randint(1, 5)
    return client_investment_objective


def generate_source_of_funding():
    client_source_of_funding = random.randint(1, 7)
    return client_source_of_funding


def generate_purpose_of_account():
    client_purpose_of_account = random.randint(1, 7)
    return client_purpose_of_account


def generate_anticipated_activity():
    client_anticipated_activity = random.randint(1, 4)
    return client_anticipated_activity


def generate_rep_id():
    n = 5
    rep_id = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=n))
    return rep_id


def generate_jurisdiction_country():
    return "United States"


def generate_acct_pass():
    word = fake.word()
    num = random.randint(1, 9999)
    return f"{word}{num}"


def acct_bal(acct_status):
    if acct_status == 0:
        return 0
    else:
        return random.randint(25000, 15000000)

# Beneficiary information
def generate_bene_cust_id():
    bene_cust_id = random.randint(100000, 1000000000)
    return str(bene_cust_id).zfill(10)


def generate_bene_relationship():
    client_bene_relationship = random.randint(1, 10)
    return client_bene_relationship


def generate_bene_ssn_front():
    area_num = fake.random_number(digits=3, fix_len=True)
    group_num = fake.random_number(digits=2, fix_len=True)
    return f"{area_num}-{group_num}"


def generate_bene_ssn_back():
    serial_num = fake.random_number(digits=4, fix_len=True)
    return serial_num


def generate_bene_portion(num_beneficiaries):
    return 100 / num_beneficiaries


# POA information
def generate_poa_cust_id(poa_random):
    poa_cust_id = random.randint(100000, 1000000000)
    if poa_random == 1:
        return str(poa_cust_id).zfill(10)
    else:
        return None


def generate_poa_role(poa_random):
    if poa_random == 1:
        client_poa = random.randint(1, 3)
        return client_poa
    else:
        return None


def generate_poa_first_name(poa_random):
    if poa_random == 1:
        return fake.first_name()
    else:
        return None


def generate_poa_last_name(poa_random):
    if poa_random == 1:
        return fake.last_name()
    else:
        return None


def generate_poa_ssn_front(poa_random):
    if poa_random == 1:
        area_num = fake.random_number(digits=3, fix_len=True)
        group_num = fake.random_number(digits=2, fix_len=True)
        return f"{area_num}-{group_num}"
    else:
        return None


def generate_poa_ssn_back(poa_random):
    if poa_random == 1:
        serial_num = fake.random_number(digits=4, fix_len=True)
        return serial_num
    else:
        return None


def generate_atm_limit():
    atm = [
        "300",
        "400",
        "500",
        "600",
        "700",
        "800",
        "900",
        "1000",
        "1500",
        "2000",
        "3000",
    ]
    return random.choice(atm)


def generate_ach_limit():
    ach = [
        "1000",
        "2000",
        "3000",
        "4000",
        "5000",
        "10000",
        "25000",
        "50000",
        "100000"
    ]
    return random.choice(ach)


def generate_wire_limit():
    wire = ["100000", "500000", "1000000", "5000000", "10000000"]
    return random.choice(wire)


def get_acct_type(generate_acct_type):
    acct_types = {
        1: ("IRA Custodial Roth", "IRA-CH"),
        2: ("Contributory IRA", "IRA-CO"),
        3: ("Education Savings", "IRA-ED"),
        4: ("Roth IRA", "IRA-RH"),
        5: ("Rollover IRA", "IRA-RO"),
        6: ("Roth Conversion IRA", "IRA-RV"),
        7: ("Simplified Employee Pension IRA", "IRA-SEP"),
        8: ("Bank One Coporate", "B1-CORP"),
        9: ("Bank One Community Property", "B1-CP"),
        10: ("Bank One Company Retirement Account", "B1-CRA"),
        11: ("Bank One Custodial", "B1-CU"),
        12: ("Bank One Individual", "B1-IND"),
        13: ("Bank One Joint Tenants with Rights of Survivorship", "B1-JT"),
        14: ("Bank One Living Trust", "B1-LT"),
        15: ("Bank One Pension Trust", "B1-PT"),
        16: ("Bank One Tenants in Common", "B1-TC"),
        17: ("Bank One Testamentary Trust", "B1-TT"),
        18: ("Bank One with High Yield Investor Checking", "B3"),
    }
    return acct_types.get(generate_acct_type)

# Employee Info


def generate_emp_suffix():
    return fake.suffix() if random.random() < 0.03 else None


def generate_middle():
    return fake.first_name() if random.random() < 0.32 else None


def generate_emp_phone():
    area_code = fake.random_number(digits=3, fix_len=True)
    central_office_code = fake.random_number(digits=3, fix_len=True)
    line_number = fake.random_number(digits=4, fix_len=True)
    return f"{area_code}-{central_office_code}-{line_number}"


def generate_ssn_front():
    area_num = fake.random_number(digits=3, fix_len=True)
    group_num = fake.random_number(digits=2, fix_len=True)
    return f"{area_num}-{group_num}"


def generate_ssn_back():
    serial_num = fake.random_number(digits=4, fix_len=True)
    return serial_num


def generate_rep_id():
    n = 5
    rep_id = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=n))
    return rep_id


def termination_reason(termination_date_math):
    if termination_date_math is None:
        return None
    else:
        return random.randint(1, 4)


def rehireable(termination_reason_result):
    if termination_reason_result in [1, 2, 3]:
        return 1
    elif termination_reason_result == 4:
        return 0


accounts_data = []

beneficiaries_data = []

joints_data = []

employees_data = []

customers_data = []

accounts_holder_data = []

cust_records = 10
emp_records = 10

for i in tqdm(range(cust_records)):
    #Customer information
    first_name = fake.first_name()
    joint_first_name = fake.first_name()
    last_name = fake.last_name()
    job = fake.job().lower()

    city, state, zip_code = random.choice(city_state_zip)

    account_holder_name = f"{first_name} {last_name}"

    start_date = datetime(1970, 1, 1)
    end_date = datetime(2023, 7, 12)
    client_since_math = start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days))

    years_to_subtract = random.randint(1, 80)
    birth_date_math = client_since_math - timedelta(days=years_to_subtract *
                                                    365)

    client_since = client_since_math.strftime("%Y-%m-%d")
    birth_date = birth_date_math.strftime("%Y-%m-%d")
    joint_birth_date = birth_date_math.strftime("%Y-%m-%d")

    if random.random() < 0.96:
        generated_num = 1
    else:
        generated_num = 0

    if random.random() < 0.96:
        generated_joint_num = 1
    else:
        generated_joint_num = 0

    employer = [
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

    employer_choice = random.choice(employer)

    sep = ","
    stripped_job = str(generate_job(generated_num)).split(sep, 1)[0]

    joint_stripped_job = str(generate_joint_job(generated_joint_num)).split(sep, 1)[0]

    cust_secondary_id = random.randint(100000, 1000000000)

    joint_secondary_id = random.randint(100000, 1000000000)

    generated_address = generate_address()

    generated_address_2 = generate_address_2()

    #Account information
    generate_acct_type = random.randint(1, 18)

    acct_type_info = get_acct_type(generate_acct_type)

    acct_type_id, (acct_type_name, acct_type_abbr) = generate_acct_type, acct_type_info

    registration_name = f"{account_holder_name} {acct_type_name}"

    account_nickname = f"{first_name} {acct_type_abbr}"

    online_banking = random.getrandbits(1)

    mobile_banking = random.getrandbits(1)

    two_factor = random.getrandbits(1)

    biometrics = random.getrandbits(1)

    voice_auth = random.getrandbits(1)

    do_not_call = random.getrandbits(1)

    share_affiliates = random.getrandbits(1)

    if random.random() < 0.15:
        poa_random = 1
    else:
        poa_random = 0

    acct_num = generate_acct_num()
    
    if random.random() < 0.96:
        acct_status = 1
    else:
        acct_status = 0

    #Generate customer data
    customer_data = {
        "cust_secondary_id": str(cust_secondary_id).zfill(10),
        "first_name": first_name,
        "middle_name": generate_middle(),
        "last_name": last_name,
        "suffix": generate_suffix(),
        "date_of_birth": birth_date,
        "client_since": client_since,
        "is_organization": generate_is_organization(),
        "id_type": generate_id_type(),
        "email": generate_email(),
        "phone_home": generate_phone_home(),
        "phone_business": generate_phone_business(),
        "address": generated_address,
        "address_2": generated_address_2,
        "city": city,
        "state": state,
        "zip_code": str(zip_code).zfill(5),
        "employment_status": generate_employment(generated_num),
        "employer_name": generate_employer(generated_num),
        "occupation": stripped_job,
        "encrypted_tax_a": generate_ssn_front(),
        "tax_b": generate_ssn_back(),
        "dl_state": state,
        "dl_num": fake.passport_number(),
        "dl_exp": generate_exp_date(),
        "mothers_maiden": fake.last_name(),
        "contact_method": generate_contact_method(),
        "voice_auth": voice_auth,
        "do_not_call": do_not_call,
        "share_affiliates": share_affiliates,
    }
    customers_data.append(customer_data)

    #Generate account data
    account_data = {
        "acct_num": acct_num,
        "cust_secondary_id": str(cust_secondary_id).zfill(10),
        "initial_contact_method": generate_initial_contact_method(),
        "acct_type": generate_acct_type,
        "registration_name": registration_name,
        "acct_objective": generate_investment_objectives(),
        "acct_funding": generate_source_of_funding(),
        "acct_purpose": generate_purpose_of_account(),
        "acct_activity": generate_anticipated_activity(),
        "acct_nickname": account_nickname,
        "rep_id": generate_rep_id(),
        "acct_status": acct_status,
        "contact_name": account_holder_name,
        "contact_address": generated_address,
        "contact_address_2": generated_address_2,
        "contact_city": city,
        "contact_state": state,
        "contact_zip": str(zip_code).zfill(5),
        "jurisdiction_country": generate_jurisdiction_country(),
        "jurisdiction_state": state,
        "acct_pass": generate_acct_pass(),
        "poa_cust_id": generate_poa_cust_id(poa_random),
        "poa_role": generate_poa_role(poa_random),
        "poa_first_name": generate_poa_first_name(poa_random),
        "poa_last_name": generate_poa_last_name(poa_random),
        "poa_encrypted_tax_a": generate_poa_ssn_front(poa_random),
        "poa_tax_b": generate_poa_ssn_back(poa_random),
        "acct_bal": acct_bal(acct_status),
        "online": online_banking,
        "mobile": mobile_banking,
        "two_factor": two_factor,
        "biometrics": biometrics,
        "atm_limit": generate_atm_limit(),
        "ach_limit": generate_ach_limit(),
        "wire_limit": generate_wire_limit(),
        "client_since": client_since,
    }
    accounts_data.append(account_data)

    #Generate joint cutomer data
    if generate_acct_type in [9, 13, 16]:
        joint_data = {
            "cust_secondary_id": str(joint_secondary_id).zfill(10),
            "joint_cust_secondary_id": str(joint_secondary_id).zfill(10),
            "first_name": joint_first_name,
            "middle_name": generate_middle(),
            "last_name": last_name,
            "suffix": generate_suffix(),
            "date_of_birth": joint_birth_date,
            "client_since": client_since,
            "is_organization": generate_is_organization(),
            "id_type": generate_id_type(),
            "email": generate_email(),
            "phone_home": generate_phone_home(),
            "phone_business": generate_phone_business(),
            "address": generated_address,
            "address_2": generated_address_2,
            "city": city,
            "state": state,
            "zip_code": str(zip_code).zfill(5),
            "employment_status": generate_employment(generated_joint_num),
            "employer_name": generate_employer(generated_joint_num),
            "occupation": joint_stripped_job,
            "encrypted_tax_a": generate_ssn_front(),
            "tax_b": generate_ssn_back(),
            "dl_state": state,
            "dl_num": fake.passport_number(),
            "dl_exp": generate_exp_date(),
            "mothers_maiden": fake.last_name(),
            "contact_method": generate_contact_method(),
            "voice_auth": voice_auth,
            "do_not_call": do_not_call,
            "share_affiliates": share_affiliates,
            "acct_num": acct_num,
        }
        customers_data.append(joint_data)
        joints_data.append(joint_data)

    #Generate beneficiary number between 1 and 4
    num_beneficiaries = random.randint(1, 4)
    for j in range(num_beneficiaries):
        bene_data = {
            "acct_num": acct_num,
            "bene_cust_id": generate_bene_cust_id(),
            "bene_first_name": fake.first_name(),
            "bene_last_name": last_name,
            "bene_encrypted_tax_a": generate_bene_ssn_front(),
            "bene_tax_b": generate_bene_ssn_back(),
            "bene_relationship": generate_bene_relationship(),
            "bene_portion": generate_bene_portion(num_beneficiaries),
            "client_since": client_since,
        }
        beneficiaries_data.append(bene_data)

for i in tqdm(range(emp_records)):
    #Employee information
    emp_first_name = fake.first_name()
    emp_last_name = fake.last_name()

    start_date = datetime(1970, 1, 1)
    end_date = datetime(2023, 7, 12)
    hire_date_math = start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days))
    years_to_subtract = random.randint(1, 80)
    birth_date_math = hire_date_math - timedelta(days=years_to_subtract * 365)

    if random.random() < 0.45:
        termination_date_math = start_date + timedelta(
            days=random.randint(0, (end_date - start_date).days))
    else:
        termination_date_math = None

    termination_reason_result = termination_reason(termination_date_math)
    rehireable_result = rehireable(termination_reason_result)

    hire_date = hire_date_math.strftime("%Y-%m-%d")
    birth_date = birth_date_math.strftime("%Y-%m-%d")

    emp_city, emp_state, emp_zip, position, salary = generate_zip_position_salary()

    emp_id = i + 1

    emp_secondary_id = i + 1

    #Generate employee data
    employee_data = {
        "emp_secondary_id": emp_secondary_id,
        "emp_first_name": emp_first_name,
        "emp_middle_name": generate_middle(),
        "emp_last_name": emp_last_name,
        "emp_suffix": generate_emp_suffix(),
        "emp_date_of_birth": birth_date,
        "rep_id": generate_rep_id(),
        "hire_date": hire_date,
        "termination_date": termination_date_math,
        "emp_email": generate_email(),
        "emp_phone": str(generate_emp_phone()),
        "emp_address": generate_emp_address(),
        "emp_address_2": generate_emp_address_2(),
        "emp_city": emp_city,
        "emp_state": emp_state,
        "emp_zip_code": str(emp_zip).zfill(5),
        "emp_encrypted_tax_a": generate_ssn_front(),
        "emp_tax_b": generate_ssn_back(),
        "effective_date": hire_date,
        "salary_amount": salary,
        "position_location_id": position,
        "start_date": hire_date,
        "end_date": termination_date_math,
        "termination_date_2": termination_date_math,
        "reason": termination_reason_result,
        "rehireable": rehireable_result,
    }
    employees_data.append(employee_data)

df_account_info = pd.DataFrame(accounts_data)
df_customer_info = pd.DataFrame(customers_data)
df_beneficiary_info = pd.DataFrame(beneficiaries_data)
df_joint_info = pd.DataFrame(joints_data)
df_employee_info = pd.DataFrame(employees_data)

#Customer information
df_customer_info = df_customer_info.sort_values("client_since")
df_customer_info["cust_id"] = range(1, len(df_customer_info) + 1)

df_cust_contact = df_customer_info[[
    "cust_id",
    "email",
    "phone_home",
    "phone_business",
    "address",
    "address_2",
    "city",
    "state",
    "zip_code",
]].copy()

df_cust_emp = df_customer_info[[
    "cust_id", "employment_status", "employer_name", "occupation"
]].copy()

df_cust_emp['employment_status'] = df_cust_emp['employment_status'].astype(str).replace('\.0', "", regex=True)

df_cust_id = df_customer_info[[
    "cust_id", "id_type", "state", "dl_num", "dl_exp", "mothers_maiden"
]].copy()

df_cust_info = df_customer_info[[
    "cust_id",
    "cust_secondary_id",
    "first_name",
    "middle_name",
    "last_name",
    "suffix",
    "date_of_birth",
    "client_since",
    "is_organization",
]].copy()

df_cust_privacy = df_customer_info[[
    "cust_id", "voice_auth", "do_not_call", "share_affiliates"
]].copy()

df_cust_tax = df_customer_info[["cust_id", "encrypted_tax_a", "tax_b"]].copy()

dataframes_cust = [
    (df_cust_contact, "cust_contact.csv"),
    (df_cust_emp, "cust_emp.csv"),
    (df_cust_id, "cust_id.csv"),
    (df_cust_info, "cust_info.csv"),
    (df_cust_privacy, "cust_privacy.csv"),
    (df_cust_tax, "cust_tax.csv"),
]

for df, filename in tqdm(dataframes_cust):
    df.to_csv(filename, index=False)


#Account information
df_account_info = df_account_info.sort_values("client_since")
df_beneficiary_info = df_beneficiary_info.sort_values("client_since")
df_account_info["acct_id"] = range(1, len(df_account_info) + 1)
df_account_info["cust_id"] = range(1, len(df_account_info) + 1)

df_acct_bal = df_account_info[["acct_id", "acct_bal"]].copy()

df_acct_bene = df_beneficiary_info[[
    "acct_num",
    "bene_cust_id",
    "bene_first_name",
    "bene_last_name",
    "bene_encrypted_tax_a",
    "bene_tax_b",
    "bene_relationship",
    "bene_portion",
    "client_since",
]].copy()

acct_num_dict = {}

for index, row in df_acct_bene.iterrows():
    acct_num = row['acct_num']
    if acct_num not in acct_num_dict:
        acct_num_dict[acct_num] = len(acct_num_dict) + 1
    df_acct_bene.at[index, 'acct_num'] = acct_num_dict[acct_num]

df_acct_bene = df_acct_bene.rename(columns={'acct_num': 'acct_id'})
df_acct_bene = df_acct_bene.drop(columns=['client_since'])

df_acct_contact = df_account_info[[
    "acct_id",
    "contact_name",
    "contact_address",
    "contact_address_2",
    "contact_city",
    "contact_state",
    "contact_zip",
]].copy()

df_acct_contact = df_acct_contact

merged_df = pd.merge(df_account_info, df_joint_info[['acct_num', 'joint_cust_secondary_id']], on='acct_num', how='left')

df_acct_holders = merged_df[[
    "acct_id", "acct_num", "cust_secondary_id", "joint_cust_secondary_id", "client_since"
]].copy()

df_acct_holders.drop(["acct_num", "client_since"], axis=1, inplace=True)

df_acct_info = df_account_info[[
    "acct_id",
    "acct_num",
    "initial_contact_method",
    "acct_type",
    "registration_name",
    "acct_objective",
    "acct_funding",
    "acct_purpose",
    "acct_activity",
    "cust_id",
    "acct_nickname",
    "rep_id",
    "client_since",
    "acct_status",
]].copy()

df_acct_jurisdiction = df_account_info[[
    "acct_id", "jurisdiction_country", "jurisdiction_state"
]].copy()

df_acct_mobile = df_account_info[[
    "acct_id", "online", "mobile", "two_factor", "biometrics"
]].copy()

df_acct_pass = df_account_info[["acct_id", "acct_pass"]].copy()

df_acct_poa = df_account_info[[
    "acct_id",
    "poa_cust_id",
    "poa_role",
    "poa_first_name",
    "poa_last_name",
    "poa_encrypted_tax_a",
    "poa_tax_b",
]].copy()

df_acct_poa.dropna(subset=["poa_cust_id"], inplace=True)

df_acct_poa['poa_role'] = df_acct_poa['poa_role'].astype(str).replace('\.0', "", regex=True)
df_acct_poa['poa_tax_b'] = df_acct_poa['poa_tax_b'].astype(str).replace('\.0', "", regex=True)

df_acct_limit = df_account_info[[
    "acct_id", "atm_limit", "ach_limit", "wire_limit"
]].copy()

dataframes_acct = [
    (df_acct_bal, "acct_bal.csv"),
    (df_acct_contact, "acct_contact.csv"),
    (df_acct_info, "acct_info.csv"),
    (df_acct_pass, "acct_pass.csv"),
    (df_acct_jurisdiction, "acct_jurisdiction.csv"),
    (df_acct_mobile, "acct_mobile.csv"),
    (df_acct_holders, "acct_holders.csv"),
    (df_acct_bene, "acct_bene.csv"),
    (df_acct_poa, "acct_poa.csv"),
    (df_acct_limit, "acct_limit.csv"),
]

for df, filename in tqdm(dataframes_acct):
    df.to_csv(filename, index=False)

#Employee information
df_employee_info = df_employee_info.sort_values("hire_date")

df_employee_info["emp_id"] = range(1, len(df_employee_info) + 1)

df_employee_info["emp_secondary_id"] = [
    f"A{i:08}" for i in range(1,
                              len(df_employee_info) + 1)
]

df_emp_contact = df_employee_info[[
    "emp_id",
    "emp_email",
    "emp_phone",
    "emp_address",
    "emp_address_2",
    "emp_city",
    "emp_state",
    "emp_zip_code",
]].copy()

df_emp_info = df_employee_info[[
    "emp_id",
    "emp_secondary_id",
    "emp_first_name",
    "emp_middle_name",
    "emp_last_name",
    "emp_suffix",
    "emp_date_of_birth",
    "rep_id",
    "hire_date",
    "termination_date",
]].copy()

df_emp_tax = df_employee_info[["emp_id", "emp_encrypted_tax_a", "emp_tax_b"]].copy()

dataframes = [
    (df_emp_contact, "emp_contact.csv"),
    (df_emp_info, "emp_info.csv"),
    (df_emp_tax, "emp_tax.csv"),
]

for df, filename in tqdm(dataframes):
    df.to_csv(filename, index=False)

df_employee_info = df_employee_info.sort_values("effective_date")

df_employee_info["salary_id"] = range(1, len(df_employee_info) + 1)

df_emp_salary = df_employee_info[[
    "salary_id", "emp_id", "effective_date", "salary_amount"
]].copy()

dataframes_salary = [
    (df_emp_salary, "emp_salary.csv"),
]

for df, filename in tqdm(dataframes_salary):
    df.to_csv(filename, index=False)

df_employee_info = df_employee_info.sort_values("start_date")

df_employee_info["emp_position_id"] = range(1, len(df_employee_info) + 1)

df_emp_position = df_employee_info[[
    "emp_position_id", "emp_id", "position_location_id", "start_date", "end_date"
]].copy()

dataframes_position = [
    (df_emp_position, "emp_position.csv"),
]

for df, filename in tqdm(dataframes_position):
    df.to_csv(filename, index=False)

df_employee_info = df_employee_info.sort_values("termination_date_2")

df_employee_info["termination_id"] = range(1, len(df_employee_info) + 1)

df_emp_termination = df_employee_info[[
    "termination_id", "emp_id", "termination_date_2", "reason", "rehireable"
]].copy()

df_emp_termination['reason'] = df_emp_termination['reason'].astype(str).replace('\.0', "", regex=True)
df_emp_termination['rehireable'] = df_emp_termination['rehireable'].astype(str).replace('\.0', "", regex=True)


df_emp_termination.dropna(subset=["termination_date_2"], inplace=True)

dataframes_termination = [
    (df_emp_termination, "emp_termination.csv"),
]

for df, filename in tqdm(dataframes_termination):
    df.to_csv(filename, index=False)

print("Data generation complete!")
