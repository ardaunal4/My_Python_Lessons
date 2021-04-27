import sqlite3

# Query The Database and Return all recors
def show_all():

    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
    conn.commit()
    conn.close()

def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("DELETE FROM customers WHERE rowid = (?)", id)

    conn.commit()
    conn.close()

def add_many(many_list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (many_list))

    conn.commit()
    conn.close()

def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))

    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()