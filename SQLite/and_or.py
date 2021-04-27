import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3") 

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()