import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# Query the Database
c.execute("SELECT rowid, * FROM customers LIMIT 2")

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()