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
df_payment = pd.read_sql("""SELECT c.contactFirstName, c.contactLastName, p.amount, p.paymentDate FROM payments AS p JOIN customers AS c ON p.customerNumber = c.customerNumber ORDER BY p.amount DESC""", conn)
df_payment['amount'] = pd.to_numeric(df_payment['amount'])
df_payment = df_payment.sort_values('amount', ascending=False)
#print(df_payment)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql("""SELECT e.employeeNumber, e.firstName, e.lastName, AVG(c.creditLimit) AS average_credit_limit FROM customers AS c JOIN employees AS e ON e.employeeNumber = c.salesRepEmployeeNumber GROUP BY e.employeeNumber HAVING average_credit_limit > 90000 ORDER BY COUNT(c.customerNumber) DESC""", conn)
#print(df_credit)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""SELECT p.productName, COUNT(o.orderNumber) AS numorders, SUM(o.quantityOrdered) AS totalunits FROM products AS p JOIN orderdetails AS o ON p.productCode = o.productCode GROUP BY p.productName ORDER BY SUM(o.quantityOrdered) DESC""", conn)
#print(df_product_sold)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""SELECT q.productName, q.productCode, COUNT(DISTINCT o.customerNumber) AS numpurchasers FROM (SELECT p.productName, p.productCode, o.orderNumber FROM products as p JOIN orderdetails AS o ON p.productCode = o.productCode) AS q JOIN orders AS o ON o.orderNumber = q.orderNumber GROUP BY q.productName ORDER BY numpurchasers DESC""", conn)
#print(df_total_customers)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""SELECT o.officeCode, SUM(q.num_of_customers) AS n_customers, o.city FROM (SELECT c.salesRepEmployeeNumber, COUNT(c.salesRepEmployeeNumber) AS num_of_customers, e.officeCode FROM customers AS c JOIN employees AS e ON e.employeeNumber = c.salesRepEmployeeNumber GROUP BY c.salesRepEmployeeNumber) AS q JOIN offices AS o ON o.officeCode = q.officeCode GROUP BY o.officeCode""", conn)
#print(df_customers)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql("""SELECT q.employeeNumber, q.firstName, q.lastName, o.city, o.officeCode FROM (SELECT e.employeeNumber, e.firstName, e.lastName, e.officeCode FROM (SELECT q.productCode, q.orderNumber, q.customerNumber, c.salesRepEmployeeNumber FROM (SELECT q.productCode, q.orderNumber, o.customerNumber FROM (SELECT q.productCode, od.orderNumber FROM (SELECT od.productCode, COUNT(DISTINCT o.customerNumber) AS num_of_customers FROM orderdetails AS od JOIN orders AS o ON o.orderNumber = od.orderNumber GROUP BY od.productCode HAVING COUNT(DISTINCT o.customerNumber) < 20) AS q JOIN orderdetails AS od ON od.productCode = q.productCode WHERE q.productCode IS NOT NULL) AS q JOIN orders AS o ON o.orderNumber = q.orderNumber) AS q JOIN customers AS c ON c.customerNumber = q.customerNumber) AS q JOIN employees AS e ON e.employeeNumber = q.salesRepEmployeeNumber) AS q JOIN offices AS o ON q.officeCode = o.officeCode GROUP BY q.employeeNumber ORDER BY q.lastName""", conn)
print(df_under_20)

conn.close()