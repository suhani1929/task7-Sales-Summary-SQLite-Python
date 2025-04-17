# task7-Sales-Summary-SQLite-Python
# 📊 Basic Sales Summary — SQLite + Python

A mini project to generate basic sales insights from a tiny SQLite database using **Python**, **pandas**, and **matplotlib**. Perfect for beginners learning SQL and data visualization!


## 🧰 What's Inside?

| File                    | Purpose                                       |
|-------------------------|-----------------------------------------------|
| `sales_data.db`         | SQLite database containing sales data         |
| `sales_summary.py`      | Python script to query + visualize the data   |
| `Sales_chart.png`       | Bar chart showing revenue by product          |
| `SQL_Query_Result.png`  | Screenshot of the SQL query output            |


## 🔍 What It Does

- Connects to an SQLite database (`sales_data.db`)
- Calculates:
  - Total quantity sold per product
  - Total revenue per product
- Prints a clean summary using `pandas`
- Generates a simple bar chart using `matplotlib`


## 📌 Example Output

🖼️ **SQL Query Result Preview:**

[SQL Query Result](SQL_Query_Result.png)

📊 **Bar Chart:**

The script generates a chart like this and saves it as `Sales_chart.png`:

[Bar Chart](Sales_chart.png)


## 🛠 Tips

- Use **DB Browser for SQLite** to view or edit your `.db` file
- Don’t forget to **click “Write Changes”** after editing
- If you get a **"database is locked"** error, make sure no other apps (like Python or Jupyter) are using it


## 🎯 Goal

A simple and visual way to practice:
- SQL queries inside Python
- Using SQLite with real data
- Basic data visualization for summaries

