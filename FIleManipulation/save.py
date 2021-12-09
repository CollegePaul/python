output = ["Mario","Yoshi","Toad"]

with open('out.txt', 'a') as f:
    f.truncate(0)
    for o in output:
        f.write(o + "\n")