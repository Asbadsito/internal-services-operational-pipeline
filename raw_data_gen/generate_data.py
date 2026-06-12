import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# --- 1. GENERATE EMPLOYEES DATA ---
print("Generating 500 perfect employees...")
employees = []
departments = ["Legal Operations", "Finance", "Compliance", "Internal Audit", "HR"]
regions = ["London", "Manchester", "Birmingham", "Bristol"]

for i in range(1, 501):
    emp_id = f"EMP{i:03d}"
    first_name = fake.first_name()
    last_name = fake.last_name()
    dept = random.choice(departments)
    region = random.choice(regions)
    hire_date = fake.date_between(start_date='-5y', end_date='today')
    
    employees.append({
        "employee_id": emp_id,
        "first_name": first_name,
        "last_name": last_name,
        "department": dept,
        "region": region,
        "hire_date": hire_date.strftime('%Y-%m-%d')
    })

# --- 2. GENERATE TICKETS DATA ---
print("Generating 5,000 compliance tickets...")
tickets = []
issue_types = ["Contract Review", "GDPR Data Breach", "Insider Trading Suspicion", "NDA Violation", "AML Alert"]
severities = ["Low", "Medium", "High", "Critical"]
statuses = ["Open", "In Progress", "Resolved", "Under Review"]

for i in range(1, 5001):
    tkt_id = f"TCK_{i:03d}"  # Matches your TCK_001 schema format perfectly
    emp_id = f"EMP{random.randint(1, 500):03d}" # Perfectly relates to generated employees
    issue = random.choice(issue_types)
    severity = random.choice(severities)
    status = random.choice(statuses)
    
    open_date = fake.date_between(start_date='-1y', end_date='today')
    resolved_date = open_date + timedelta(days=random.randint(2, 25)) if status == "Resolved" else None
    if resolved_date and resolved_date > datetime.today().date():
        resolved_date = None
        
    risk_score = random.randint(10, 100)
    
    tickets.append({
        "ticket_id": tkt_id,
        "employee_id": emp_id,
        "issue_type": issue,
        "severity": severity,
        "status": status,
        "created_date": open_date.strftime('%Y-%m-%d'),
        "resolved_date": resolved_date.strftime('%Y-%m-%d') if resolved_date else "",
        "risk_score": risk_score
    })

# Save clean lowercase files matching your postgres columns perfectly
pd.DataFrame(employees).to_csv("dim_employees.csv", index=False)
pd.DataFrame(tickets).to_csv("fact_compliance_tickets.csv", index=False)
print("CSV files generated successfully!")
