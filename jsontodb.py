import sqlite3
import json
com=sqlite3.connect('new.db') #creating New database
cur=com.cursor()  #creating cursor a control structure
cur.executescript('''
DROP TABLE IF EXISTS Employee;

CREATE TABLE IF NOT EXISTS Employee
	(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Name TEXT,
    Age INTEGER NOT NULL,
    Gender TEXT
);
''')
name = input('Enter file name:') #getting the json file
sdata = open(name).read() #reading the file and storing as string data
data = json.loads(sdata) #loading json data into list
print (data)
for entry in data:
    name = entry[1]
    age = entry[0]
    gen=entry[2]
    print(name,age,gen)
    cur.execute('''INSERT OR IGNORE INTO Employee(Name, Age, Gender) VALUES ( ?,?,?)''', (name, age,gen) )
    com.commit()  #saving the database
com.close()   #closing the database
