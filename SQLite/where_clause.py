import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# Query the Database
# c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()