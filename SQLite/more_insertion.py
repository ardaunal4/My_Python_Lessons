import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

many_costumers = [('Wes', 'Brown', 'wes@brown.com'),
                  ('Steph', 'Curi', 'steph@curi.com'),
                  ('Alan', 'Walker', 'alan@walker.com'),
                  ('Arda', 'Unal', 'ardaunal4@gmail.com'),
                  ('Abdulrezzak', 'Kirilmis', '27fucker@hotmail.com')]
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_costumers)

conn.commit()

conn.close()