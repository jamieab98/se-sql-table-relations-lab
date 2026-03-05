# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""SELECT employees.firstName, employees.lastName, employees.jobTitle FROM employees JOIN offices ON employees.officeCode = offices.officeCode WHERE offices.city = 'Boston'""", conn)
#print(df_boston)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""SELECT officeCode, COUNT(*) AS number_of_employees FROM employees GROUP BY officeCode HAVING number_of_employees IS 0""", conn)
#print(df_zero_emp)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""SELECT e.firstName, e.lastName, o.city, o.state FROM employees AS e JOIN offices as o ON e.officeCode = o.officeCode ORDER BY e.firstName ASC, e.lastName ASC""", conn)
#print(df_employee)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber FROM customers AS c LEFT JOIN orders AS o ON o.customerNumber = c.customerNumber WHERE o.orderNumber IS NULL ORDER BY c.contactLastName""" , conn)
#print(df_contacts)

# STEP 5
# Replace None with your code
df_payment = None

# STEP 6
# Replace None with your code
df_credit = None

# STEP 7
# Replace None with your code
df_product_sold = None

# STEP 8
# Replace None with your code
df_total_customers = None

# STEP 9
# Replace None with your code
df_customers = None

# STEP 10
# Replace None with your code
df_under_20 = None

conn.close()