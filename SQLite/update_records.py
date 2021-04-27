import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("""UPDATE customers SET first_name = 'John' 
             WHERE last_name = 'Elder' """)
             
conn.commit()

c.execute(""" UPDATE customers SET first_name = 'Ahmad' WHERE rowid = 4""")
conn.commit()
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()
for item in items:
    print(item)

conn.commit()

conn.close()