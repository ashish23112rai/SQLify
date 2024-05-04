import sqlite3

connection=sqlite3.connect("student.db")

#creating cursor

cursor=connection.cursor()

#create table

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

#Insert some more records 

cursor.execute('''Insert Into STUDENT values('Ashish','Data Science','A',100)''')
cursor.execute('''Insert Into STUDENT values('Adarsh','DEVOPS','B',50)''')
cursor.execute('''Insert Into STUDENT values('Salik','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Abhishek','DEVOPS','A',40)''')
cursor.execute('''Insert Into STUDENT values('Anurag','Data Science','A',80)''')

#Display all the records

print("The inserted records are")

data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

#Close the connection
connection.commit()
connection.close()

