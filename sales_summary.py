import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the existing DB
conn = sqlite3.connect("sales_data.db")

# Query to summarize sales
query = """
    SELECT
          product,
          SUM(quantity) AS total_qty,
          ROUND(SUM(quantity * price), 2) AS revenue
    FROM sales
    GROUP BY product
"""
# Load data into DataFrame
df = pd.read_sql_query(query, conn)

# Print Summary
print("Sales Summary : \n")
print(df)

# Plot revenue per product
df.plot(kind = 'bar', x = 'product', y = 'revenue', color = 'skyblue', legend = False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("Sales_chart.png")
plt.show()

conn.close()

