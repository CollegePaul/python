#python dictionary

#Lists are accessed by the position in the list, an index
#Dictionaries are accessed by a key

games = dict([
    ('minecraft', 'mojang'),
    ('terraria','Re-Logic'),
    ('Nintendogs', "Nintendo"),
    ('Super Mario Bros', 'Nintendo')
])

print(games)
print(games['Super Mario Bros'])

games['Pac-Man'] = 'Namco'

del games['Nintendogs']

print(games)

if 'minecraft' in games:
    print('Yep minecraft is in the dictionary')

print(games.keys())

print(games.values())

