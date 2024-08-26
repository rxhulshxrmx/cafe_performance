import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import os

# Initialize Faker
fake = Faker()

# Set a random seed based on the current date for variety
np.random.seed(int(datetime.now().timestamp()))

def generate_daily_sales():
    today = datetime.now().date()
    bill_number = int(pd.read_csv('cafe_sales.csv')['Bill Number'].str[1:].max()) + 1
    
    num_sales = np.random.randint(50, 100) if today.weekday() < 5 else np.random.randint(80, 150)
    data = []
    
    for _ in range(num_sales):
        item = np.random.choice(['Coffee', 'Tea', 'Pastry', 'Sandwich', 'Salad'])
        quantity = np.random.randint(1, 4)
        rate = np.random.choice([2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0])
        subtotal = quantity * rate
        tax = round(subtotal * 0.08, 2)
        discount = round(subtotal * np.random.choice([0, 0.05, 0.1]), 2)
        total = subtotal + tax - discount
        
        data.append({
            'Date': today,
            'Bill Number': f'B{bill_number}',
            'Item Description': item,
            'Time': fake.time(),
            'Quantity': quantity,
            'Rate': rate,
            'Tax': tax,
            'Discount': discount,
            'Total': round(total, 2),
            'Category': 'Food' if item in ['Pastry', 'Sandwich', 'Salad'] else 'Beverage'
        })
        bill_number += 1
    
    return pd.DataFrame(data)

def generate_daily_expenses():
    today = datetime.now().date()
    categories = ['Ingredients', 'Utilities', 'Rent', 'Salaries', 'Maintenance', 'Marketing']
    data = []
    for category in categories:
        data.append({
            'date': today,
            'category': category,
            'amount': np.random.uniform(50, 500) if category != 'Rent' else np.random.uniform(1000, 1500)
        })
    return pd.DataFrame(data)

def generate_daily_attendance():
    today = datetime.now().date()
    data = []
    for hour in range(6, 22):
        data.append({
            'date': today,
            'hour': hour,
            'attendance': np.random.randint(5, 50)
        })
    return pd.DataFrame(data)

# Generate and append daily data
daily_sales = generate_daily_sales()
daily_expenses = generate_daily_expenses()
daily_attendance = generate_daily_attendance()

# Append to existing CSV files
daily_sales.to_csv('cafe_sales.csv', mode='a', header=False, index=False)
daily_expenses.to_csv('cafe_expenses.csv', mode='a', header=False, index=False)
daily_attendance.to_csv('cafe_attendance.csv', mode='a', header=False, index=False)

print(f"Daily data for {datetime.now().date()} appended to CSV files.")