import sqlite3

conn = sqlite3.connect('company.db')

curs = conn.cursor()

curs.execute('create table employee(name, age)')
curs.execute("insert into employee values ('Ali', 28)")
values = [('Brad',54), ('Ross', 34), ('Muhammad', 28), ('Bilal', 44)]
curs.executemany('insert into employee values(?,?)', values)
conn.commit()
conn.close
