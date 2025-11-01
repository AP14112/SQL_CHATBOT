import sqlite3
connection=sqlite3.connect("student.db")
cursor=connection.cursor()

table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""
cursor.execute(table_info)

cursor.execute("insert into STUDENT values('Ravi','ai','A',85)")
cursor.execute("insert into STUDENT values('Raj','ml','B',75)")
cursor.execute("insert into STUDENT values('Ramesh','dl','A',95)")
cursor.execute("insert into STUDENT values('Rohan','ai','C',65)")
cursor.execute("insert into STUDENT values('Rahul','ml','B',55)")

print("The inserted data are:")
data=cursor.execute("select * from STUDENT")
for row in data:
    print(row)
connection.commit()
connection.close()
