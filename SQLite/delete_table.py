import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("DROP TABLE customers")
conn.commit()

# Query the Database
c.execute("SELECT rowid, * FROM customers ")

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()