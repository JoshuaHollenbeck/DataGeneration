from tqdm import tqdm
from faker import Faker
from datetime import datetime, timedelta
import random
import pandas as pd

fake = Faker("en_US")

def generate_acct_number()
    random.randint(10000000,99999999)


all_data = []

records = 5
for i in tqdm(range(records)):
    first_name = fake.first_name()
    last_name = fake.last_name()
    job = fake.job().lower()

    start_date = datetime(1970, 1, 1)
    end_date = datetime(2023, 7, 12)
    client_since_math = start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days)
    )

    years_to_subtract = random.randint(1, 80)
    birth_date_math = client_since_math - timedelta(days=years_to_subtract * 365)

    client_since = client_since_math.strftime("%Y-%m-%d")
    birth_date = birth_date_math.strftime("%Y-%m-%d")
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
    second_email = random.choice([name for name in first_email if name != first_choice])
    third_email = birth_year
    if random.random() < 0.36:
        forth_choice = third_email
    else:
        forth_choice = ""
    email = f"{first_choice}{random.choice(spacing_email)}{second_email}{forth_choice}{domain_name}"

    if random.random() < 0.96:
        generated_num = 1
    else:
        generated_num = 0

    employer = [
        fake.first_name().title() + " " + fake.company_suffix(),
        fake.last_name().title() + " " + fake.company_suffix(),
        fake.safe_color_name().title() + " " + fake.word().title() + " " + fake.company_suffix(),
        fake.safe_color_name().title() + " " + fake.company_suffix(),
        fake.word().title() + " " + fake.safe_color_name().title() + " " + fake.company_suffix(),
        fake.word().title() + " " + fake.company_suffix(),
        fake.street_suffix().title() + " " + fake.company_suffix(),
        fake.last_name().title() + " & Sons",
        fake.first_name().title() + " & Sons",
    ]

    employer_choice = random.choice(employer)

    sep = ","
    stripped_job = str(generate_job(generated_num)).split(sep, 1)[0]

    cust_secondary_id = random.randint(100000, 1000000000)

    state = fake.state_abbr(include_territories = True, include_freely_associated_states = False)

    all_data.append(
        [
            acct_num"
            inital_contact_method,
            acct_type,
            registration_name,
            investment_objectives,
            source_of_funding,
            purpose_of_account,
            anticipated_activity,
            rep_id,
            established_date,
            acct_status,
            tax_withholding_code,
            primary_contact_name,
            primary_contact_address,
            primary_contact_city,
            primary_contact_state,
            primary_contact_zip,
            jurisdiction_country,
            jurisdiction_state,
            acct_pass,
            acct_funding,
            acct_purpose,
            anticipated_activity,
            acct_holder_name,
            acct_holder_role,
            acct_holder_tax_id,
            acct_holder_cust_id,        
            beneficiary_name,
            beneficiary_tax_id,
            beneficiary_relationship,
            beneficiary_portion,
            power_of_attorney_role,
            power_of_attorney_name,
            power_of_attorney_tax_id,
            
            str(cust_secondary_id).zfill(10),
            first_name,
            generate_middle(),
            last_name,
            generate_suffix(),
            birth_date,
            client_since,
            email,
            generate_phone(),
            generate_address(),
            generate_address_2(),
            fake.city(),
            state,
            fake.postcode().zfill(5),
            generate_employment(generated_num),
            generate_employer(generated_num),
            stripped_job,
            generate_ssn_front(),
            generate_ssn_back(),
            state,
            fake.passport_number(),
            generate_exp_date(),
            fake.last_name(),
            generate_contact_method(),
            generate_voice_auth(),
            generate_do_not_call(),
            generate_share_affiliates(),
        ]
    )

df_all_data = pd.DataFrame(
    all_data,
    columns=[
        "acct_num"
        "inital_contact_method",
        "acct_type",
        "registration_name",
        "investment_objectives",
        "source_of_funding",
        "purpose_of_account",
        "anticipated_activity",
        "rep_id",
        "established_date",
        "acct_status",
        "tax_withholding_code",
        "primary_contact_name",
        "primary_contact_address",
        "primary_contact_city",
        "primary_contact_state",
        "primary_contact_zip",
        "jurisdiction_country",
        "jurisdiction_state",
        "acct_pass",
        "acct_funding",
        "acct_purpose",
        "anticipated_activity",
        "acct_holder_name",
        "acct_holder_role",
        "acct_holder_tax_id",
        "acct_holder_cust_id",        
        "beneficiary_name",
        "beneficiary_tax_id",
        "beneficiary_relationship",
        "beneficiary_portion",
        "power_of_attorney_role",
        "power_of_attorney_name",
        "power_of_attorney_tax_id",        
    ],
)

df_all_data = df_all_data.sort_values("established_date")
df_all_data["acct_id"] = range(1, len(df_all_data) + 1)

df_acct_info = df_all_data[[
    "acct_id",
    "acct_num",
    "inital_contact_method",
    "acct_type",
    "registration_name",
    "investment_objectives",
    "source_of_funding",
    "purpose_of_account",
    "anticipated_activity",
    "rep_id",
    "established_date",
    "acct_status",
    "tax_withholding_code"]].copy()
df_acct_contact = df_all_data[[
    "acct_id",
    "primary_contact_name",
    "primary_contact_address",
    "primary_contact_city",
    "primary_contact_state",
    "primary_contact_zip"]].copy()
df_acct_jurisdiction = df_all_data[[
    "acct_id",
    "jurisdiction_country",
    "jurisdiction_state",].copy()
df_acct_pass = df_all_data[[
    "acct_id",
    "acct_pass"]].copy()
df_acct_holders = df_all_data[[
    "acct_id",
    "acct_holder_name",
    "acct_holder_role",
    "acct_holder_tax_id",
    "acct_holder_cust_id"]].copy()
df_acct_beneficiaries = df_all_data[[
    "acct_id",
    "beneficiary_name",
    "beneficiary_tax_id",
    "beneficiary_relationship",
    "beneficiary_portion"]].copy()
df_acct_power_of_attorney = df_all_data[[
    "acct_id",
    "power_of_attorney_role",
    "power_of_attorney_name",
    "power_of_attorney_tax_id"]].copy()

dataframes = [
    (df_acct_info, "acct_info.csv"),
    (df_acct_pass, "acct_pass.csv"),
    (df_acct_type, "acct_type.csv"),
    (df_acct_mailing, "acct_mailing.csv"),
    (df_acct_contact, "acct_contact.csv"),
    (df_acct_jurisdiction, "acct_jurisdiction.csv"),
    (df_acct_holders, "acct_holders.csv"),
    (df_acct_beneficiaries, "acct_beneficiaries.csv"),
    (df_acct_power_of_attorney, "acct_power_of_attorney.csv"),
]

for df, filename in tqdm(dataframes):
    df.to_csv(filename, index=False)

print("Data generation complete!")
