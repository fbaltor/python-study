import sqlite3


conn = sqlite3.connect('datafile.db')
cursor = conn.cursor()
print(cursor)

cursor.execute("create table people (id integer primary key, name text, count integer)")
cursor.execute("insert into people (name, count) values ('Bob', 1)")
cursor.execute("insert into people (name, count) values (?, ?)", ("Jill", 15))
conn.commit()

result = cursor.execute("select * from people")
print(result.fetchall())
