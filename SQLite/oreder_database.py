import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC") # tersinden okumak
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name") # ASCII alfabesine gore siraliyor
c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC") # ASCII alfabesine gore ters siraliyor

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()