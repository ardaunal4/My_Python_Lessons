import sqlite3

#conn = sqlite3.connect(":memory:") # work with memory! 
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Crate a table

c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text)
    """)
# Data types = NULL, INTEGER, REAL, TEXT, BLOB

# Commit our comand
conn.commit()

# Close our connection
conn.close()