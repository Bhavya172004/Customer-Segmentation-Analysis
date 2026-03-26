import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv", encoding='latin1')

# Check columns (for understanding)
print("Columns:", df.columns)

# Data Cleaning
df = df.dropna()
df = df.drop_duplicates()

# Revenue per customer
customer_revenue = df.groupby('CUSTOMERNAME')['SALES'].sum().reset_index()

# Segmentation logic
def segment(x):
    if x > 5000:
        return "High Value"
    elif x > 2000:
        return "Medium Value"
    else:
        return "Low Value"

# Apply segmentation
customer_revenue['Segment'] = customer_revenue['SALES'].apply(segment)

# Save output
customer_revenue.to_csv("output.csv", index=False)

print("Project Completed ✅")

import matplotlib.pyplot as plt

# Count of segments
customer_revenue['Segment'].value_counts().plot(kind='bar')

plt.title("Customer Segmentation")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")

plt.show()