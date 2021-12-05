
lines = []

with open('text.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())