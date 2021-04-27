import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# Query the Database
c.execute("SELECT rowid, * FROM customers")
"""
print(c.fetchone()[0]) # fetch last item from the table
#c.fetchmany(3)
print(c.fetchall())
"""
items = c.fetchall()
for item in items:
    print(item[0])

conn.commit()

conn.close()