import csv

newData = []

with open('games.csv', 'r') as f:
    data = list(csv.reader(f))

    #newData.append(data[0])  #header
    
    for row in range(1, len(data)):
        studio = data[row][4].strip()
        studio = studio.upper()
        newData.append([data[row][0], studio])
    
with open("newGames.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for row in newData:
        writer.writerow(row)


