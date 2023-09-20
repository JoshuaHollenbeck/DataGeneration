from tqdm import tqdm
from faker import Faker
from datetime import datetime, timedelta
from _city_info import *
from _trade_info import *
import time
import random
import math
import string
import pandas as pd
import copy

random.seed(time.time())
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

def generate_is_organization():
    return 1 if random.random() < 0 else 0

generated_cust_id = set()

def generate_secondary_id(num):
    while True:  # Infinite loop to keep generating until a unique number is found.
        if num == 1:
            cust_id = random.randint(100000, 1000000000)            

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

# Account information
generated_acct_nums = set()

def generate_acct_nums(acct_type_id):
    # Infinite loop to keep generating until a unique number is found.
    while True:
        if acct_type_id in range(1, 8):
            acct_num = random.randint(10000000, 25999999)
        elif acct_type_id in range(8, 16):
            acct_num = random.randint(26000000, 49999999)
        elif acct_type_id == 16:
            acct_num = int(f"4000{random.randint(50000000, 75999999)}")
        else:
            acct_num = int(f"6000{random.randint(76000000, 99999999)}")

        if acct_num not in generated_acct_nums:
            generated_acct_nums.add(acct_num)
            return acct_num

def get_acct_status():
    if random.random() < 0.96:
        acct_status = 1
    else:
        acct_status = 0
    
    return acct_status

def get_closed_date(acct_status):
    if acct_status == 1:
        closed_date = closed_date_math.strftime("%Y-%m-%d")
    else:
        closed_date = None
    
    return closed_date

def get_closest_branch():
    closest_branch = None
    
    # Initialize min_distance with infinity to ensure any subsequent distance is smaller
    min_distance = float('inf')

    # Loop through all company locations
    for comp_location in comp_zips:
        comp_id, _, _, _, _, _, lat2, lon2, type_id = comp_location
        
        # Calculate the distance from the current location to a given point using the haversine formula
        distance = haversine_distance(lat1, lon1, lat2, lon2)
        
        # Check if the current location is of type 'branch'
        if type_id == 2:
            # If the current distance is the smallest encountered so far, update min_distance and closest_branch
            if distance < min_distance:
                min_distance = distance
                closest_branch = comp_id
   
    # Return the ID of the closest branch found
    return closest_branch

def generate_contact_method():
    return 1 if random.random() < 0.34 else None

def generate_investment_objectives():
    cust_investment_objective = random.randint(1, 5)
    return cust_investment_objective

def generate_source_of_funding():
    cust_source_of_funding = random.randint(1, 7)
    return cust_source_of_funding

def generate_purpose_of_account():
    cust_purpose_of_account = random.randint(1, 7)
    return cust_purpose_of_account

def generate_anticipated_activity():
    cust_anticipated_activity = random.randint(1, 4)
    return cust_anticipated_activity

def generate_jurisdiction_country():
    return 1

def generate_acct_pass():
    word = fake.word()
    num = random.randint(1, 9999)
    return f"{word}{num}"

def acct_bal(acct_status):
    acct_bal_value = round(random.uniform(5000.00, 10000.00), 2)
    if acct_status == 0:
        return 0
    else:
        return acct_bal_value

# Use haversine formula to compute the distance between two sets of latitudes and longitudes
def haversine_distance(lat1, lon1, lat2, lon2):
    # Earth's radius in kilometers
    R = 6371
    
    # Convert the difference in latitudes from degrees to radians
    dlat = math.radians(lat2 - lat1)

    # Convert the difference in longitudes from degrees to radians
    dlon = math.radians(lon2 - lon1)
    
    # Calculate the square of half the chord length between the two points using Haversine formula
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    
    # Compute the angular distance in radians
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Convert the angular distance from radians to actual distance using the Earth's radius
    distance = R * c
    
    return distance

def generate_rep_id(rep_status):
    n = 5
    rep_id = "".join(random.choices(
        string.ascii_uppercase + string.digits, k=n))

    if rep_status == 'trade':
        return rep_id if random.random() < 0.03 else None
    if rep_status == '4':
        return rep_id
    if rep_status == 'employee':
        if main_client == 1:
            return rep_id
        else:
            return None
    else:
        None

def generate_atm_limits():
    atm_limits = [
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
    return random.choice(atm_limits)

def generate_ach_limits():
    ach_limits = [
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
    return random.choice(ach_limits)

def generate_wire_limits():
    wire_limits = [
        "100000",
        "500000",
        "1000000",
        "5000000",
        "10000000"
    ]
    return random.choice(wire_limits)

def get_acct_types(acct_type):
    acct_types = {
        1: ("IRA Custodial Roth", "IRA-CH"),
        2: ("Contributory IRA", "IRA-CO"),
        3: ("Education Savings", "IRA-ED"),
        4: ("Roth IRA", "IRA-RH"),
        5: ("Rollover IRA", "IRA-RO"),
        6: ("Roth Conversion IRA", "IRA-RV"),
        7: ("Simplified Employee Pension IRA", "IRA-SEP"),
        8: ("Community Property", "J1-CP"),
        9: ("Custodial", "J1-CU"),
        10: ("Individual", "J1-IND"),
        11: ("Joint Tenants with Rights of Survivorship", "J1-JT"),
        12: ("Living Trust", "J1-LT"),
        13: ("Pension Trust", "J1-PT"),
        14: ("Tenants in Common", "J1-TC"),
        15: ("Testamentary Trust", "J1-TT"),
        16: ("Investor Checking", "J2-IC"),
        17: ("Investor Savings", "J2-IS")
    }
    return acct_types.get(acct_type)

# Beneficiary information
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

# POA information
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

# Transactions
def get_transaction_types(transaction_type):
    transaction_types = {
        1: (1, "Deposit", "DEP"),
        2: (2, "Withdrawal", "WDL"),
        3: (3, "Buy", "BUY"),
        4: (4, "Sell", "SELL"),
        5: (5, "Check", "CHK"),
        6: (6, "Debit Card", "DBT"),
        7: (7, "Credit Card", "CRD"),
        8: (8, "Journal", "JRNL"),
        9: (9, "Interest Earned", "I-E"),
        10: (10, "ACH", "ACH"),
        11: (11, "Wire", "WIR"),
    }
    return transaction_types.get(transaction_type)

def generate_transaction_dates():
    generated_dates = []
    num_transactions = random.randint(1000, 5000)

    for i in range(num_transactions):  # Generate range of dates
        transaction_date = cust_since + timedelta(days=random.randint(0, (closed_date - cust_since).days))
        generated_dates.append(transaction_date)

    generated_dates.sort()  # Sort range of dates from earliest to latest
    
    return generated_dates

def get_transaction_details(acct_type):
    ira_transaction_type_list = [3, 4]
    brokerage_transaction_type_list = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
    checking_transaction_type_list = [1, 2, 5, 6, 7, 10, 11]
    savings_transaction_type_list = [1, 2, 5, 9, 10, 11]

    if acct_type in range(1, 8):
        type_list = ira_transaction_type_list
        amt_min, amt_max = 50.00, 5000.00
    elif acct_type in range(8, 16):
        type_list = brokerage_transaction_type_list
        amt_min, amt_max = 50.00, 1000.00
    elif acct_type == 16:
        type_list = checking_transaction_type_list
        amt_min, amt_max = 25.00, 100.00
    else:
        type_list = savings_transaction_type_list
        amt_min, amt_max = None, None

    transaction_type = random.choice(type_list)
    transaction_info = get_transaction_types(transaction_type)
    
    return transaction_type, transaction_info, amt_min, amt_max

def generate_transactions(acct_num, acct_type, generated_dates, acct_bal_value):
    temp_transactions = []
    stock_info = {}
    final_acct_balances = {}

    for transaction_date in generated_dates:
        trade_status = "5"
        trade_fees = "00.00"
        currency = "USD"
        transaction_date_str = transaction_date.strftime("%Y-%m-%d")
        stock_exchange, stock_id, trade_price = generate_trade()
        sell_quantity = random.randint(1, 5)

        if acct_type in range (1,8):
            transaction_type, transaction_info, amt_min, amt_max = get_transaction_details(acct_type)
            if transaction_info[0] == 4:
                transaction_amt = round(sell_quantity * trade_price, 2)
            else:
                transaction_amt = round(random.uniform(amt_min, amt_max), 2)
            buy_quantity = round(transaction_amt / trade_price, 4)
            
            if transaction_info[0] == 3:  # Buy
                transaction_data = {
                    "acct_num": acct_num,
                    "acct_type": acct_type,
                    "transaction_type": transaction_info[0],
                    "transaction_amt": transaction_amt,
                    "transaction_date": transaction_date_str,
                    "stock_exchange": stock_exchange,
                    "stock_id": stock_id,
                    "trade_quantity": buy_quantity,
                    "trade_price": trade_price,
                    "trade_amount": transaction_amt,
                    "trade_status": trade_status,
                    "trade_fees": trade_fees,
                    "currency": currency,
                    "rep_id": generate_rep_id('trade')
                }
                temp_transactions.append(transaction_data)

                if stock_id not in stock_info:
                    stock_info[stock_id] = {"quantity": 0, "total_cost": 0.0}

                stock_info[stock_id]["quantity"] += buy_quantity
                stock_info[stock_id]["total_cost"] += transaction_amt

            elif transaction_info[0] == 4:  # Sell
                transaction_data = {
                    "acct_num": acct_num,
                    "acct_type": acct_type,
                    "transaction_type": transaction_info[0],
                    "transaction_amt": transaction_amt,
                    "transaction_date": transaction_date_str,
                    "stock_exchange": stock_exchange,
                    "stock_id": stock_id,
                    "trade_quantity": sell_quantity,
                    "trade_price": trade_price,
                    "trade_amount": transaction_amt,
                    "trade_status": trade_status,
                    "trade_fees": trade_fees,
                    "currency": currency,
                    "rep_id": generate_rep_id('trade')
                }
                temp_transactions.append(transaction_data)

                if stock_id in stock_info:
                    stock_info[stock_id]["quantity"] -= sell_quantity
                    stock_info[stock_id]["total_cost"] -= transaction_amt

            else:
                transaction_data = {
                    "acct_num": acct_num,
                    "acct_type": acct_type,
                    "transaction_type": transaction_info[0],
                    "transaction_amt": transaction_amt,
                    "transaction_date": transaction_date_str,
                }
                temp_transactions.append(transaction_data)

        elif acct_type in range (8, 16):
            transaction_type, transaction_info, amt_min, amt_max = get_transaction_details(acct_type)
            if transaction_info[0] == 4:
                transaction_amt = round(sell_quantity * trade_price, 2)
            else:
                transaction_amt = round(random.uniform(amt_min, amt_max), 2)
            buy_quantity = round(transaction_amt / trade_price, 4)

            if transaction_info[0] == 3:  # Buy
                transaction_data = {
                    "acct_num": acct_num,
                    "acct_type": acct_type,
                    "transaction_type": transaction_info[0],
                    "transaction_amt": transaction_amt,
                    "transaction_date": transaction_date_str,
                    "stock_exchange": stock_exchange,
                    "stock_id": stock_id,
                    "trade_quantity": buy_quantity,
                    "trade_price": trade_price,
                    "trade_amount": transaction_amt,
                    "trade_status": trade_status,
                    "trade_fees": trade_fees,
                    "currency": currency,
                    "rep_id": generate_rep_id('trade')
                }
                temp_transactions.append(transaction_data)

                if stock_id not in stock_info:
                    stock_info[stock_id] = {"quantity": 0, "total_cost": 0.0}

                stock_info[stock_id]["quantity"] += buy_quantity
                stock_info[stock_id]["total_cost"] += transaction_amt

            elif transaction_info[0] == 4:  # Sell
                transaction_data = {
                    "acct_num": acct_num,
                    "acct_type": acct_type,
                    "transaction_type": transaction_info[0],
                    "transaction_amt": transaction_amt,
                    "transaction_date": transaction_date_str,
                    "stock_exchange": stock_exchange,
                    "stock_id": stock_id,
                    "trade_quantity": sell_quantity,
                    "trade_price": trade_price,
                    "trade_amount": transaction_amt,
                    "trade_status": trade_status,
                    "trade_fees": trade_fees,
                    "currency": currency,
                    "rep_id": generate_rep_id('trade')
                }
                temp_transactions.append(transaction_data)

                if stock_id in stock_info:
                    stock_info[stock_id]["quantity"] -= sell_quantity
                    stock_info[stock_id]["total_cost"] -= transaction_amt

            else:
                transaction_data = {
                    "acct_num": acct_num,
                    "acct_type": acct_type,
                    "transaction_type": transaction_info[0],
                    "transaction_amt": transaction_amt,
                    "transaction_date": transaction_date_str,
                }
                temp_transactions.append(transaction_data)

        elif acct_type == 16:
            transaction_type, transaction_info, amt_min, amt_max = get_transaction_details(acct_type)
            transaction_amt = round(random.uniform(amt_min, amt_max), 2)
            buy_quantity = round(transaction_amt / trade_price, 4)

            transaction_data = {
                "acct_num": acct_num,
                "acct_type": acct_type,
                "transaction_type": transaction_info[0],
                "transaction_amt": transaction_amt,
                "transaction_date": transaction_date_str,
            }
            temp_transactions.append(transaction_data)

        else:
            transaction_type, transaction_info, amt_min, amt_max = get_transaction_details(acct_type)

            if transaction_info[0] == 9:
                savings_transaction_amt = round(acct_bal_value * 0.0045, 2)
            else:
                savings_transaction_amt = round(random.uniform(25.00, 50.00), 2)

            transaction_data = {
                "acct_num": acct_num,
                "acct_type": acct_type,
                "transaction_type": transaction_info[0],
                "transaction_amt": savings_transaction_amt,
                "transaction_date": transaction_date_str,
            }
            temp_transactions.append(transaction_data)
    
    # First loop for preprocessing transactions based on running_balance
    running_balance = acct_bal_value
    for transaction in temp_transactions:
        transaction_type = transaction["transaction_type"]
        transaction_amt = transaction["transaction_amt"]
        acct_num = transaction["acct_num"]

        if running_balance <= 1000:
            transaction["transaction_type"] = 4
            transaction_amt = round(random.uniform(1000.00, 5000.00), 2)
            transaction["transaction_amt"] = transaction_amt

        if transaction["transaction_type"] == 4:
            running_balance += transaction_amt
        else:
            running_balance -= transaction_amt

    # Second loop for actually processing transactions
    for transaction in temp_transactions:
        acct_num = transaction["acct_num"]
        # Capture the current balance as the previous balance before modifying it
        previous_bal = acct_bal_value

        transaction_type = transaction["transaction_type"]
        transaction_amt = transaction["transaction_amt"]

        if transaction_type == 4:
            acct_bal_value += transaction_amt
        else:
            acct_bal_value -= transaction_amt

        # Proceed with setting transaction and balance details
        final_acct_balances[acct_num] = round(acct_bal_value, 2)
        transaction["transaction_id"] = len(transactions_data) + 1
        transaction["pre_bal"] = round(previous_bal, 2)
        transaction["post_bal"] = round(acct_bal_value, 2)
        transactions_data.append(transaction)

    return stock_info, final_acct_balances

def holding_total(stock_info):
     for stock_id in stock_info:
        if stock_info[stock_id]["quantity"] > 0:
            average_cost = stock_info[stock_id]["total_cost"] / stock_info[stock_id]["quantity"]
        else:
            average_cost = 0.0

        holding_data = {
            "acct_num": acct_num,
            "acct_type": acct_type,
            "stock_id": stock_id,
            "quantity": round(stock_info[stock_id]["quantity"], 4),
            "average_cost": round(average_cost, 2)
        }
        holdings_data.append(holding_data)

accounts_data = []

beneficiaries_data = []

joints_data = []

employees_data = []

customers_data = []

transactions_data = []

holdings_data = []

# Number of records to generate
cust_records = 10
emp_records = 10

# tqdm Customization
def format_desc(text, length=55):
    return f"{text:.<{length}}"

bar_format = "{desc:<55}: {percentage:3.0f}%|{bar:100}| {n_fmt}/{total_fmt} | [{remaining}]"

# Generate custs
for i in tqdm(range(cust_records), desc=format_desc("Generating Customers"), bar_format=bar_format):
    # Customer information
    first_name = fake.first_name()
    joint_first_name = fake.first_name()    
    last_name = fake.last_name()
    is_cust = 1
    is_joint = 1
    
    # Customer city state zip lat and lon
    chosen_city = random.choice(city_info)
    zip_id, city, state, state_id, zip, lat1, lon1 = chosen_city

    cust_since, birth_date, joint_birth_date, closed_date_math, emp_birth_date, hire_date, termination_date_math = generate_dates()

    generated_num = generate_num()
    joint_generated_num = generate_num()

    employer_choice = generate_employer(generated_num)
    joint_employer_choice = generate_employer(joint_generated_num)

    generated_address = generate_address()
    generated_address_2 = generate_address_2()

    cust_secondary_id = generate_secondary_id(is_cust)
    joint_secondary_id = generate_secondary_id(is_joint)

    # Account information
    account_holder_name = f"{first_name} {last_name}"
    online_banking = random.getrandbits(1)
    mobile_banking = random.getrandbits(1)
    two_factor = random.getrandbits(1)
    biometrics = random.getrandbits(1)
    voice_auth = random.getrandbits(1)
    do_not_call = random.getrandbits(1)
    share_affiliates = random.getrandbits(1)  
    
    # Get the closest branch
    closest_branch = get_closest_branch()
    
    # Generate power of attorney chances 
    poa_num = generate_poa_chance()

    # Get acct closure status
    acct_status = get_acct_status()
    closed_date = get_closed_date(acct_status)

    # Number of accts to create per customer
    num_of_accts = random.randint(1, 5)

    # Generate customer data
    customer_data = {
        "cust_secondary_id": str(cust_secondary_id).zfill(10),
        "first_name": first_name,
        "middle_name": generate_middle(),
        "last_name": last_name,
        "suffix": generate_suffix(),
        "date_of_birth": birth_date,
        "client_since": cust_since,
        "is_organization": generate_is_organization(),
        "id_type": generate_id_types(),
        "cust_email": generate_email(),
        "cust_phone_home": generate_phone_home(),
        "cust_phone_business": generate_phone_business(),
        "cust_address": generated_address,
        "cust_address_2": generated_address_2,
        "cust_city": city,
        "cust_state": state_id,
        "cust_zip": zip_id,
        "cust_country": generate_jurisdiction_country(),
        "employment_status": generate_employment_status(generated_num),
        "employer_name": employer_choice,
        "occupation": generate_job(generated_num),
        "tax_id": generate_tax_id(is_cust),
        "dl_num": fake.passport_number(),
        "dl_exp": generate_exp_date(),
        "mothers_maiden": fake.last_name(),
        "contact_method": generate_contact_method(),
        "voice_auth": voice_auth,
        "do_not_call": do_not_call,
        "share_affiliates": share_affiliates,
    }
    customers_data.append(customer_data)

    # Generate account data
    for j in range(num_of_accts):
        # Generate acct type and acct type info
        generate_acct_type = random.randint(1, 17)
        acct_type_info = get_acct_types(generate_acct_type)
        acct_type_id, (acct_type_name, acct_type_abbr) = generate_acct_type, acct_type_info

        acct_num = generate_acct_nums(generate_acct_type)

        registration_name = f"{account_holder_name} {acct_type_name}"
        
        account_nickname = f"{first_name} {acct_type_abbr}"
        
        initial_contact = random.choice(["1", "2", "3", "4"])
             
        account_data = {
            "acct_num": acct_num,
            "cust_secondary_id": str(cust_secondary_id).zfill(10),
            "initial_contact_method": initial_contact,
            "acct_type": generate_acct_type,
            "registration_name": registration_name,
            "acct_objective": generate_investment_objectives(),
            "acct_funding": generate_source_of_funding(),
            "acct_purpose": generate_purpose_of_account(),
            "acct_activity": generate_anticipated_activity(),
            "acct_nickname": account_nickname,
            "rep_id": generate_rep_id(initial_contact),
            "acct_status": acct_status,
            "closed_date": closed_date,
            "contact_name": account_holder_name,
            "contact_address": generated_address,
            "contact_address_2": generated_address_2,
            "contact_city": city,
            "contact_state": state_id,
            "contact_zip": zip_id,
            "jurisdiction_country": generate_jurisdiction_country(),
            "jurisdiction_state": state_id,
            "acct_pass": generate_acct_pass(),
            "poa_cust_id": generate_secondary_id(poa_num),
            "poa_role": generate_poa_role(poa_num),
            "poa_first_name": generate_poa_first_name(poa_num),
            "poa_last_name": generate_poa_last_name(poa_num),
            "poa_tax_id": generate_tax_id(poa_num),
            "acct_bal": acct_bal(acct_status),
            "online": online_banking,
            "mobile": mobile_banking,
            "two_factor": two_factor,
            "biometrics": biometrics,
            "atm_limit": generate_atm_limits(),
            "ach_limit": generate_ach_limits(),
            "wire_limit": generate_wire_limits(),
            "client_since": cust_since,
            "acct_branch_id": closest_branch
        }
        accounts_data.append(account_data)

    # Generate joint cutomer data if acct_type is joint
    if generate_acct_type in [8, 11, 14]:
        joint_data = {
            "cust_secondary_id": str(joint_secondary_id).zfill(10),
            "joint_cust_secondary_id": str(joint_secondary_id).zfill(10),
            "first_name": joint_first_name,
            "middle_name": generate_middle(),
            "last_name": last_name,
            "suffix": generate_suffix(),
            "date_of_birth": joint_birth_date,
            "client_since": cust_since,
            "is_organization": generate_is_organization(),
            "id_type": generate_id_types(),
            "cust_email": generate_joint_email(),
            "cust_phone_home": generate_phone_home(),
            "cust_phone_business": generate_phone_business(),
            "cust_address": generated_address,
            "cust_address_2": generated_address_2,
            "cust_city": city,
            "cust_state": state_id,
            "cust_zip": zip_id,
            "cust_country": generate_jurisdiction_country(),
            "employment_status": generate_employment_status(joint_generated_num),
            "employer_name": joint_employer_choice,
            "occupation": generate_job(joint_generated_num),
            "tax_id": generate_tax_id(is_cust),
            "dl_state": state_id,
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

    # Generate beneficiary number between 1 and 4
    num_beneficiaries = random.randint(1, 4)
    has_bene = 1

    for l in range(num_beneficiaries):
        bene_data = {
            "acct_num": acct_num,
            "bene_cust_id": generate_secondary_id(has_bene),
            "bene_first_name": fake.first_name(),
            "bene_last_name": last_name,
            "bene_tax_id": generate_tax_id(has_bene),
            "bene_relationship": generate_bene_relationship(),
            "bene_portion": generate_bene_portion(num_beneficiaries),
            "client_since": cust_since,
        }
        beneficiaries_data.append(bene_data)

# Generate transactions
for account in tqdm(accounts_data, desc=format_desc("Generating Transactions"), bar_format=bar_format):
    acct_num = account["acct_num"]
    acct_type = account["acct_type"]
    acct_bal_value = account["acct_bal"]
    cust_since = datetime.strptime(account["client_since"], "%Y-%m-%d")
    closed_date = datetime.strptime(account["closed_date"], "%Y-%m-%d") if account["closed_date"] else datetime.now()
    
    generated_dates = generate_transaction_dates()
    
    stock_info, final_acct_balances = generate_transactions(acct_num, acct_type, generated_dates, acct_bal_value)
    
    holding_total(stock_info)

# Generate employees
for i in tqdm(range(emp_records), desc=format_desc("Generating Employees"), bar_format=bar_format):
    # Employee information
    emp_first_name = fake.first_name()
    emp_last_name = fake.last_name()

    cust_since, birth_date, joint_birth_date, closed_date_math, emp_birth_date, hire_date, termination_date_math = generate_dates() 
    
    termination_reason_result = get_termination_reason(termination_date_math)
    rehireable_result = get_rehireable(termination_reason_result)
    emp_city, emp_state_id, emp_zip_id, position, main_client, salary = generate_zip_position_salary()
    emp_id = i + 1
    emp_secondary_id = i + 1
    is_emp = 1

    # Generate employee data
    employee_data = {
        "emp_secondary_id": emp_secondary_id,
        "emp_first_name": emp_first_name,
        "emp_middle_name": generate_middle(),
        "emp_last_name": emp_last_name,
        "emp_suffix": generate_emp_suffix(),
        "emp_date_of_birth": emp_birth_date,
        "rep_id": generate_rep_id('employee'),
        "hire_date": hire_date,
        "termination_date": termination_date_math,
        "emp_email": generate_email(),
        "emp_phone": str(generate_emp_phone()),
        "emp_address": generate_emp_address(),
        "emp_address_2": generate_emp_address_2(),
        "emp_city": emp_city,
        "emp_state": emp_state_id,
        "emp_zip": emp_zip_id,
        "emp_tax_id": generate_tax_id(is_emp),
        "effective_date": hire_date,
        "salary_amount": salary,
        "position_location_id": position,
        "mc_access": main_client,
        "start_date": hire_date,
        "end_date": termination_date_math,
        "termination_date_2": termination_date_math,
        "reason": termination_reason_result,
        "rehireable": rehireable_result,
        "emp_pass": generate_emp_pass()
    }
    employees_data.append(employee_data)

def create_dataframe_with_tqdm(data, name):
    desc = format_desc(f"Creating {name}")
    for i in tqdm(range(1), desc=desc, bar_format=bar_format):
        df = pd.DataFrame(data)
    return df

# Generate Dataframes
df_account_info = create_dataframe_with_tqdm(accounts_data, "Account Info Dataframe")

df_customer_info = create_dataframe_with_tqdm(customers_data, "Customer Info Dataframe")

df_beneficiary_info = create_dataframe_with_tqdm(beneficiaries_data, "Beneficiary Info Dataframe")

df_joint_info = create_dataframe_with_tqdm(joints_data, "Joint Info Dataframe")

df_employee_info = create_dataframe_with_tqdm(employees_data, "Customer Info Dataframe")

df_transaction_info = create_dataframe_with_tqdm(transactions_data, "Transaction Info Dataframe")

df_holding_info = create_dataframe_with_tqdm(holdings_data, "Holding Info Dataframe")

# Customer information
for i in tqdm(range(1), desc=format_desc("Sorting Customer Info"), bar_format=bar_format):
    df_customer_info = df_customer_info.sort_values("client_since")

for i in tqdm(range(1), desc=format_desc("Assigning Customer ID"), bar_format=bar_format):
    df_customer_info["cust_id"] = range(1, len(df_customer_info) + 1)

df_cust_contact = df_customer_info[[
    "cust_id",
    "cust_email",
    "cust_phone_home",
    "cust_phone_business",
    "cust_address",
    "cust_address_2",
    "cust_city",
    "cust_state",
    "cust_zip",
    "cust_country"
]].copy()

for i in tqdm(range(1), desc=format_desc("Converting Customer Contact Decimal to String"), bar_format=bar_format):
    df_cust_contact['cust_city'] = df_cust_contact['cust_city'].astype(str).replace('\.0', "", regex=True)

    df_cust_contact['cust_country'] = df_cust_contact['cust_country'].astype(str).replace('\.0', "", regex=True)

dataframes_cust_contact = [
    (df_cust_contact, "cust_contact.csv"),
]

df_cust_emp = df_customer_info[[
    "cust_id",
    "employment_status",
    "employer_name",
    "occupation"
]].copy()

for i in tqdm(range(1), desc=format_desc("Converting Customer Employee Decimal to String"), bar_format=bar_format):
    df_cust_emp['employment_status'] = df_cust_emp['employment_status'].astype(str).replace('\.0', "", regex=True)

dataframes_cust_emp = [
    (df_cust_emp, "cust_emp.csv"),
]

df_cust_id = df_customer_info[[
    "cust_id",
    "id_type",
    "cust_state",
    "dl_num",
    "dl_exp",
    "mothers_maiden"
]].copy().rename(columns={"cust_state": "id_state"})

dataframes_cust_id = [
    (df_cust_id, "cust_id.csv"),
]

df_cust_info = df_customer_info[[
    "cust_id",
    "cust_secondary_id",
    "first_name",
    "middle_name",
    "last_name",
    "suffix",
    "date_of_birth",
    "client_since",
    "is_organization"
]].copy()

dataframes_cust_info = [
    (df_cust_info, "cust_info.csv"),
]

df_cust_privacy = df_customer_info[[
    "cust_id",
    "voice_auth",
    "do_not_call",
    "share_affiliates"
]].copy()

dataframes_cust_privacy = [
    (df_cust_privacy, "cust_privacy.csv"),
]

df_cust_tax = df_customer_info[[
    "cust_id",
    "tax_id",
]].copy()

dataframes_cust_tax = [
    (df_cust_tax, "cust_tax.csv")
]

for df, filename in tqdm(dataframes_cust_contact, desc=format_desc("Creating cust_contact.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_cust_emp, desc=format_desc("Creating cust_emp.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_cust_id, desc=format_desc("Creating cust_id.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_cust_info, desc=format_desc("Creating cust_info.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_cust_privacy, desc=format_desc("Creating cust_privacy.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_cust_tax, desc=format_desc("Creating cust_tax.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

# Account information
for i in tqdm(range(1), desc=format_desc("Sorting Account Info"), bar_format=bar_format):
    df_account_info = df_account_info.sort_values("client_since")

for i in tqdm(range(1), desc=format_desc("Sorting Beneficiary Info"), bar_format=bar_format):
    df_beneficiary_info = df_beneficiary_info.sort_values("client_since")

for i in tqdm(range(1), desc=format_desc("Sorting Transaction Info"), bar_format=bar_format):
    df_transaction_info = df_transaction_info.sort_values("transaction_date")

for i in tqdm(range(1), desc=format_desc("Sorting Trade Info"), bar_format=bar_format):
    df_transaction_info = df_transaction_info.sort_values("transaction_date")

for i in tqdm(range(1), desc=format_desc("Assigning acct_id to Account Info"), bar_format=bar_format):
    df_account_info["acct_id"] = range(1, len(df_account_info) + 1)

for i in tqdm(range(1), desc=format_desc("Assigning cust_id to Account Info"), bar_format=bar_format):
    df_account_info["cust_id"] = range(1, len(df_account_info) + 1)

for i in tqdm(range(1), desc=format_desc("Assigning bene_id to Account Info"), bar_format=bar_format):
    df_beneficiary_info["bene_id"] = range(1, len(df_beneficiary_info) + 1)

for i in tqdm(range(1), desc=format_desc("Assigning poa_id to Account Info"), bar_format=bar_format):
    df_account_info["poa_id"] = range(1, len(df_account_info) + 1)

for i in tqdm(range(1), desc=format_desc("Assigning transaction_id to Account Transactions"), bar_format=bar_format):
    df_transaction_info["transaction_id"] = range(1, len(df_transaction_info) + 1)

for i in tqdm(range(1), desc=format_desc("Assigning trade_id to Account Trade"), bar_format=bar_format):
    df_transaction_info["trade_id"] = range(1, len(df_transaction_info) + 1)

for i in tqdm(range(1), desc=format_desc("Assigning holding_id to Account Holding"), bar_format=bar_format):
    df_holding_info["holding_id"] = range(1, len(df_holding_info) + 1)

for acct_num, final_bal in tqdm(final_acct_balances.items(), desc=format_desc("Updating Account Balance"), bar_format=bar_format):
    df_account_info.loc[df_account_info['acct_num'] == acct_num, 'acct_bal'] = final_bal

df_acct_bal = df_account_info[[
    "acct_id",
    "acct_bal"
]].copy()

df_acct_bene = df_beneficiary_info[[
    "bene_id",
    "acct_num",
    "bene_cust_id",
    "bene_first_name",
    "bene_last_name",
    "bene_tax_id",
    "bene_relationship",
    "bene_portion",
    "client_since",
]].copy()

bene_acct_num_dict = {}

for index, row in tqdm(df_acct_bene.iterrows(), total=df_acct_bene.shape[0], desc=format_desc("Updating Beneficiary Account Number to Account ID"), bar_format=bar_format):
    acct_num = row['acct_num']
    if acct_num not in bene_acct_num_dict:
        bene_acct_num_dict[acct_num] = len(bene_acct_num_dict) + 1
    df_acct_bene.at[index, 'acct_num'] = bene_acct_num_dict[acct_num]

for i in tqdm(range(1), desc=format_desc("Renaming Account Number to Account ID"), bar_format=bar_format):
    df_acct_bene = df_acct_bene.rename(columns={'acct_num': 'acct_id'})

for i in tqdm(range(1), desc=format_desc("Dropping Client Since"), bar_format=bar_format):
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

for i in tqdm(range(1), desc=format_desc("Joining Joint Info to Account Holders"), bar_format=bar_format):
    if df_joint_info.empty:
        merged_df = df_account_info.copy()
        merged_df['joint_cust_secondary_id'] = 'NONE'
    else:
        merged_df = pd.merge(df_account_info, df_joint_info[['acct_num', 'joint_cust_secondary_id']], on='acct_num', how='left')

df_acct_holders = merged_df[[
    "acct_id",
    "acct_num",
    "cust_secondary_id",
    "joint_cust_secondary_id",
    "client_since"
]].copy()

for i in tqdm(range(1), desc=format_desc("Dropping Account Number and Client Since"), bar_format=bar_format):
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
    "client_since",
    "acct_status",
    "closed_date",
    "rep_id"
]].copy()

df_acct_jurisdiction = df_account_info[[
    "acct_id",
    "jurisdiction_country",
    "jurisdiction_state"
]].copy()

df_acct_mobile = df_account_info[[
    "acct_id",
    "online",
    "mobile",
    "two_factor",
    "biometrics"
]].copy()

df_acct_pass = df_account_info[[
    "acct_id",
    "acct_pass"
]].copy()

df_acct_poa = df_account_info[[
    "poa_id",
    "acct_id",
    "poa_cust_id",
    "poa_role",
    "poa_first_name",
    "poa_last_name",
    "poa_tax_id",
]].copy()

for i in tqdm(range(1), desc=format_desc("Dropping Empty Power of Attorney Rows"), bar_format=bar_format):
    df_acct_poa.dropna(subset=["poa_cust_id"], inplace=True)

for i in tqdm(range(1), desc=format_desc("Converting Power of Attorney Decimal to String"), bar_format=bar_format):
    df_acct_poa['poa_role'] = df_acct_poa['poa_role'].astype(str).replace('\.0', "", regex=True)

df_acct_limit = df_account_info[[
    "acct_id",
    "atm_limit",
    "ach_limit",
    "wire_limit"
]].copy()

df_acct_transaction = df_transaction_info[[
    "transaction_id",
    "acct_num",
    "acct_type",
    "transaction_type",
    "transaction_amt",
    "transaction_date",
    "pre_bal",
    "post_bal",
    "trade_amount"
]].copy()

df_acct_branch = df_account_info[[
    "acct_id",
    "acct_branch_id"
]].copy()

df_acct_trade = df_transaction_info[[
    "trade_id",
    "acct_num",
    "acct_type",
    "transaction_date",
    "transaction_type",
    "stock_exchange",
    "stock_id",
    "trade_quantity",
    "trade_price",
    "trade_amount",
    "trade_status",
    "trade_fees",
    "currency",
    "rep_id"
]].copy()

df_acct_holding = df_holding_info[[
    "holding_id",
    "acct_num",
    "acct_type",
    "stock_id",
    "quantity",
    "average_cost"
]].copy()

transaction_acct_num_dict = {}

for index, row in tqdm(df_acct_transaction.iterrows(), total=df_acct_transaction.shape[0], desc=format_desc("Updating Transaction Account Number to Account ID"), bar_format=bar_format):
    acct_num = row['acct_num']
    if acct_num not in transaction_acct_num_dict:
        transaction_acct_num_dict[acct_num] = len(
            transaction_acct_num_dict) + 1
    df_acct_transaction.at[index, 'acct_num'] = transaction_acct_num_dict[acct_num]

df_acct_transaction = df_acct_transaction.rename(
    columns={'acct_num': 'acct_id'})

trade_acct_num_dict = {}

for index, row in tqdm(df_acct_trade.iterrows(), total=df_acct_trade.shape[0], desc=format_desc("Updating Trade Account Number to Account ID"), bar_format=bar_format):
    acct_num = row['acct_num']
    if acct_num not in trade_acct_num_dict:
        trade_acct_num_dict[acct_num] = len(trade_acct_num_dict) + 1
    df_acct_trade.at[index, 'acct_num'] = trade_acct_num_dict[acct_num]

df_acct_trade = df_acct_trade.rename(columns={'acct_num': 'acct_id'})

stock_holdings_dict = {}

for index, row in tqdm(df_acct_holding.iterrows(), total=df_acct_holding.shape[0], desc=format_desc("Updating Stock Holding Account Number to Account ID"), bar_format=bar_format):
    acct_num = row['acct_num']
    if acct_num not in stock_holdings_dict:
        stock_holdings_dict[acct_num] = len(stock_holdings_dict) + 1
    df_acct_holding.at[index, 'acct_num'] = stock_holdings_dict[acct_num]

df_acct_holding = df_acct_holding.rename(columns={'acct_num': 'acct_id'})

for i in tqdm(range(1), desc=format_desc("Dropping Empty Acct Holding Rows"), bar_format=bar_format):
    df_acct_holding.drop(
        df_acct_holding[df_acct_holding['quantity'] < 0].index, inplace=True)

dataframes_acct_bal = [
    (df_acct_bal, "acct_bal.csv")
]

dataframes_acct_contact = [
    (df_acct_contact, "acct_contact.csv")
]

dataframes_acct_info = [
    (df_acct_info, "acct_info.csv")
]

dataframes_acct_pass = [
    (df_acct_pass, "acct_pass.csv")
]

dataframes_acct_jurisdiction = [
    (df_acct_jurisdiction, "acct_jurisdiction.csv")
]

dataframes_acct_mobile = [
    (df_acct_mobile, "acct_mobile.csv")
]

dataframes_acct_holders = [
    (df_acct_holders, "acct_holders.csv")
]

dataframes_acct_bene = [
    (df_acct_bene, "acct_bene.csv")
]

dataframes_acct_poa = [
    (df_acct_poa, "acct_poa.csv")
]

dataframes_acct_limit = [
    (df_acct_limit, "acct_limit.csv")
]

dataframes_acct_transaction = [
    (df_acct_transaction, "acct_transaction.csv")
]

dataframes_acct_branch = [
    (df_acct_branch, "acct_branch.csv")
]

dataframes_acct_trade = [
    (df_acct_trade, "acct_trade.csv")
]

dataframes_acct_holdings = [
    (df_acct_holding, "acct_holding.csv")
]

for df, filename in tqdm(dataframes_acct_bal, desc=format_desc("Creating acct_bal.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_contact, desc=format_desc("Creating acct_contact.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_info, desc=format_desc("Creating acct_info.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_pass, desc=format_desc("Creating acct_pass.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_jurisdiction, desc=format_desc("Creating acct_jurisdiction.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_mobile, desc=format_desc("Creating acct_mobile.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_holders, desc=format_desc("Creating acct_holders.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_bene, desc=format_desc("Creating acct_bene.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_poa, desc=format_desc("Creating acct_poa_.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_limit, desc=format_desc("Creating acct_limit.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_transaction, desc=format_desc("Creating acct_transaction.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_branch, desc=format_desc("Creating acct_branch.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_trade, desc=format_desc("Creating acct_trade.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_acct_holdings, desc=format_desc("Creating acct_holding.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

# Employee information

for i in tqdm(range(1), desc=format_desc("Sorting Employee Info"), bar_format=bar_format):
    df_employee_info = df_employee_info.sort_values("hire_date")

for i in tqdm(range(1), desc=format_desc("Assigning Employee ID"), bar_format=bar_format):
    df_employee_info["emp_id"] = range(1, len(df_employee_info) + 1)

for i in tqdm(range(1), desc=format_desc("Assigning Employee Secondary ID"), bar_format=bar_format):
    df_employee_info["emp_secondary_id"] = [f"A{i:08}" for i in range(1, len(df_employee_info) + 1)]

df_emp_contact = df_employee_info[[
    "emp_id",
    "emp_email",
    "emp_phone",
    "emp_address",
    "emp_address_2",
    "emp_city",
    "emp_state",
    "emp_zip",
]].copy()

df_emp_info = df_employee_info[[
    "emp_id",
    "emp_secondary_id",
    "emp_first_name",
    "emp_middle_name",
    "emp_last_name",
    "emp_suffix",
    "emp_date_of_birth",
    "hire_date",
    "termination_date",
]].copy()

df_emp_pass = df_employee_info[[
    "emp_id",
    "emp_pass"
]].copy()

for i in tqdm(range(1), desc=format_desc("Dropping Empty Employee Password Rows"), bar_format=bar_format):
    df_emp_pass.dropna(subset=["emp_pass"], inplace=True)

df_emp_tax = df_employee_info[[
    "emp_id",
    "emp_tax_id"
]].copy()

df_emp_rep_id = df_employee_info[[
    "emp_id",
    "rep_id",
]].copy()

dataframes_emp_contact = [
    (df_emp_contact, "emp_contact.csv")
]

dataframes_emp_info = [
    (df_emp_info, "emp_info.csv")
]

dataframes_emp_pass = [
    (df_emp_pass, "emp_pass.csv"),
]

dataframes_emp_tax = [
    (df_emp_tax, "emp_tax.csv")
]

dataframes_emp_rep_id = [
    (df_emp_rep_id, "emp_rep_id.csv")
]

for df, filename in tqdm(dataframes_emp_contact, desc=format_desc("Creating emp_contact.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_emp_info, desc=format_desc("Creating emp_info.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_emp_pass, desc=format_desc("Creating emp_pass.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_emp_tax, desc=format_desc("Creating emp_tax.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for df, filename in tqdm(dataframes_emp_rep_id, desc=format_desc("Creating emp_rep_id.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

# for i in tqdm(range(1), desc=format_desc("Sorting Employee Info"), bar_format=bar_format):
#     df_employee_info = df_employee_info.sort_values("emp_id")

for i in tqdm(range(1), desc=format_desc("Assinging Salary ID"), bar_format=bar_format):
    df_employee_info["salary_id"] = range(1, len(df_employee_info) + 1)

df_emp_salary = df_employee_info[[
    "salary_id",
    "emp_id",
    "effective_date",
    "termination_date",
    "salary_amount"
]].copy()

dataframes_emp_salary = [(df_emp_salary, "emp_salary.csv"),]

for df, filename in tqdm(dataframes_emp_salary, desc=format_desc("Creating emp_salary.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

# for i in tqdm(range(1), desc=format_desc("Sorting Employee Start Date"), bar_format=bar_format):
#     df_employee_info = df_employee_info.sort_values("emp_id")

for i in tqdm(range(1), desc=format_desc("Assigning Employee Position ID"), bar_format=bar_format):
    df_employee_info["emp_position_id"] = range(1, len(df_employee_info) + 1)

df_emp_position = df_employee_info[[
    "emp_position_id",
    "emp_id",
    "position_location_id",
    "start_date",
    "end_date",
    "mc_access"
]].copy()

dataframes_emp_position = [
    (df_emp_position, "emp_position.csv"),
]

for df, filename in tqdm(dataframes_emp_position, desc=format_desc("Creating emp_position.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

for i in tqdm(range(1), desc=format_desc("Sorting Termination Info"), bar_format=bar_format):
    df_employee_info = df_employee_info.sort_values("termination_date_2")

for i in tqdm(range(1), desc=format_desc("Assigning Employee Termindation ID"), bar_format=bar_format):
    df_employee_info["termination_id"] = range(1, len(df_employee_info) + 1)

df_emp_termination = df_employee_info[[
    "termination_id",
    "emp_id",
    "termination_date_2",
    "reason",
    "rehireable"
]].copy()

for i in tqdm(range(1), desc=format_desc("Converting Employee Decimal to String"), bar_format=bar_format):
    df_emp_termination['reason'] = df_emp_termination['reason'].astype(str).replace('\.0', "", regex=True)

    df_emp_termination['rehireable'] = df_emp_termination['rehireable'].astype(str).replace('\.0', "", regex=True)

for i in tqdm(range(1), desc=format_desc("Dropping Termination Date Column"), bar_format=bar_format):
    df_emp_termination.dropna(subset=["termination_date_2"], inplace=True)

dataframes_emp_termination = [(df_emp_termination, "emp_termination.csv"),]

for df, filename in tqdm(dataframes_emp_termination, desc=format_desc("Creating emp_termination.csv"), bar_format=bar_format):
    df.to_csv(filename, index=False)

print("Data generation complete!")
