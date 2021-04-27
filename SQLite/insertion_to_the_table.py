import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")

conn.commit()

conn.close()