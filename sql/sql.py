import sqlite3

connection = sqlite3.connect("test.db")

cursor = connection.cursor()

# #make database if it does not exist
# command1 = "CREATE TABLE IF NOT EXISTS main(person_id INTEGER PRIMARY KEY, fname TEXT, job TEXT)"
# cursor.execute(command1)

# #add values into the talel
# cursor.execute("INSERT INTO main VALUES (1, 'Paul', 'Smith')")
# cursor.execute("INSERT INTO main VALUES (2, 'Albus', 'Dog')")

# #make the data permanent
# connection.commit() 

#retrieve datas

#all persons
cursor.execute("SELECT * FROM main")
results = cursor.fetchall()
print("ALL: " , results)


#a person by id
cursor.execute("SELECT * FROM main WHERE person_id = 2")
results = cursor.fetchall()
print("Just ID 2: ", results)