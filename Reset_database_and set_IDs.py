import sqlite3 as base
# create or connect a data base
data_base = base.connect("demo1.db")
# create a cursor
cursor = data_base.cursor()



cursor.execute("delete from CUSTOMER")
cursor.execute("delete from CUSTOMER_Address")
cursor.execute("delete from ACCOUNT")
cursor.execute("delete from OFFICER")
cursor.execute("delete from OFFICER_ADDRESS")
cursor.execute("delete from TRANSACTIONS")

cursor.execute("select * from account")
print(cursor.fetchall())
data_base.commit()
data_base.close()