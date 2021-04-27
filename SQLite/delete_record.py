import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute(" DELETE from customers WHERE rowid = 4 ")
             
conn.commit()

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()