import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Set a random seed for reproducibility
np.random.seed(42)

# Generate date range for one year
start_date = datetime(2023, 1, 1)
date_range = [start_date + timedelta(days=x) for x in range(365)]

# Generate sales data
def generate_sales_data(date_range):
    data = []
    bill_number = 1000  # Starting bill number
    for date in date_range:
        # Generate more sales for weekends
        num_sales = np.random.randint(50, 100) if date.weekday() < 5 else np.random.randint(80, 150)
        for _ in range(num_sales):
            item = np.random.choice(['Coffee', 'Tea', 'Pastry', 'Sandwich', 'Salad'])
            quantity = np.random.randint(1, 4)
            rate = np.random.choice([2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0])
            subtotal = quantity * rate
            tax = round(subtotal * 0.08, 2)  # Assuming 8% tax
            discount = round(subtotal * np.random.choice([0, 0.05, 0.1]), 2)  # 0%, 5%, or 10% discount
            total = subtotal + tax - discount
            
            data.append({
                'Date': date,
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

# Generate expenses data
def generate_expenses_data(date_range):
    categories = ['Ingredients', 'Utilities', 'Rent', 'Salaries', 'Maintenance', 'Marketing']
    data = []
    for date in date_range:
        for category in categories:
            data.append({
                'date': date,
                'category': category,
                'amount': np.random.uniform(50, 500) if category != 'Rent' else np.random.uniform(1000, 1500)
            })
    return pd.DataFrame(data)

# Generate attendance data
def generate_attendance_data(date_range):
    data = []
    for date in date_range:
        # Generate hourly attendance
        for hour in range(6, 22):  # Assume café opens from 6 AM to 10 PM
            data.append({
                'date': date,
                'hour': hour,
                'attendance': np.random.randint(5, 50)
            })
    return pd.DataFrame(data)

# Generate the datasets
sales_df = generate_sales_data(date_range)
expenses_df = generate_expenses_data(date_range)
attendance_df = generate_attendance_data(date_range)

# Save to CSV
sales_df.to_csv('cafe_sales.csv', index=False)
expenses_df.to_csv('cafe_expenses.csv', index=False)
attendance_df.to_csv('cafe_attendance.csv', index=False)

print("Data generation complete. Files saved: cafe_sales.csv, cafe_expenses.csv, cafe_attendance.csv")