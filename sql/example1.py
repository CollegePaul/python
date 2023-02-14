#example of using SQL and python

import sqlite3

connection = sqlite3.connect("mydb.db")

cursor = connection.cursor()

def makeTable():

    #make database table if it does not exist
    #the SQL will make a table called main, add an id, name, and colour field
    command1 = "CREATE TABLE IF NOT EXISTS main(id INTEGER PRIMARY KEY, name TEXT, colour TEXT)"
    cursor.execute(command1)

    #add values into the table
    cursor.execute("INSERT INTO main VALUES (1, 'Mario', 'Red')")
    cursor.execute("INSERT INTO main VALUES (2, 'Luigi', 'Green')")
    cursor.execute("INSERT INTO main VALUES (3, 'Bowser', 'Purple')")#
    cursor.execute("INSERT INTO main VALUES (4, 'Wario', 'Yellow')")

    #make the data permanent
    connection.commit() 

#run the function to make the table
#makeTable()
cursor.execute("INSERT INTO main VALUES (1, 'Wario', 'Yellow')")

#all persons
cursor.execute("SELECT * FROM main")
results = cursor.fetchall()
print("ALL: " , results)

#1 record of a person by id
cursor.execute("SELECT * FROM main WHERE id = 2")
results = cursor.fetchall()
print("Just ID 2: ", results)

