import sqlite3

connection = sqlite3.connect("test3.db")

cursor = connection.cursor()


def makeDB():
    #make database if it does not exist
    command1 = "CREATE TABLE IF NOT EXISTS main(ID_Person INTEGER PRIMARY KEY, Type TEXT, colour TEXT)"
    cursor.execute(command1)

    # command2 = "CREATE TABLE IF NOT EXISTS main(ID_colour INTEGER PRIMARY KEY, colour TEXT)"
    # cursor.execute(command2)

    #add values into the table
    cursor.execute("INSERT INTO main VALUES (1, 'Paul', 'Smith')")
    cursor.execute("INSERT INTO main VALUES (2, 'Albus', 'Dog')")

    #make the data permanent
    connection.commit() 

#retrieve datas
makeDB()


#all persons
cursor.execute("SELECT * FROM main")
results = cursor.fetchall()
print("ALL: " , results)


#a person by id
cursor.execute("SELECT * FROM main WHERE ID_Person = 2")
results = cursor.fetchall()
print("Just ID 2: ", results)