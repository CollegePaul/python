'''In this programe we will load the data from a file,
   process it and save it in a database'''
import sqlite3

database = "game.db"


#load the data from file
def loadDataFromFile():
    lines = [] #data in
    output = [] #data in array for saving to database
    with open('in.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip('\n') #remove the newline character if present
        game = line.split(",")
        for g in range(0,len(game)):
            game[g] = game[g].lstrip()
        print(game) #for testing

        output.append(game)  
    return output


def makeDB(data):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    #make database if it does not exist
    command1 = """CREATE TABLE IF NOT EXISTS games
                  (game_id INTEGER PRIMARY KEY,
                   game_name TEXT,
                   studio TEXT,
                   games_sold int,
                   year int)"""
    cursor.execute(command1)

    #add values into the table line by line
    id = 0
    for d in data:
        sql_param = """INSERT INTO games
                                    (game_id,game_name,studio,games_sold,year)
                                    VALUES (?,?,?,?,?)
                                    """
        #a tuple with the data
        data_to_enter = (id,d[0],d[1],d[2],d[3])
        id+=1
        cursor.execute(sql_param, data_to_enter)
        #make the data permanent
        connection.commit() 
    
    cursor.close()
    connection.close()



def getLine(id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    #a fame by id
    cursor.execute("SELECT * FROM games WHERE game_id =" + str(id))
    results = cursor.fetchall()
   
    cursor.close()
    connection.close()

    print(results)

    return results
    


def get_by_studio(studio):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    #get by studio
    cursor.execute("SELECT * FROM games WHERE studio = 'Nintendo'")
    results = cursor.fetchall()
   
    cursor.close()
    connection.close()

    print(results)

    return results


'''Program start'''

#on first set up run these two lines
#filedata = loadDataFromFile()
#makeDB(filedata)

#get a line by id
getLine(0)

#get all the nintendo games, and add the total sold games
nList = get_by_studio("Nintendo")
total = 0
for n in nList:
    total = total + int(n[3])
print(total)



