from csvclass import CSVloader

#a static version of the loader could also be made.

c = CSVloader("games.csv")
result = c.loadFile_list()
print(result)