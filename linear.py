#linear search
names = ["Luigi","Yoshi","Toad","Mario","Daisy"]

def linear_search(term, list):
    found = False
    for i in range(0,len(list)):
        if term == list[i]:
            found = True
            break
    if found:
        return "found"
    else:
        return "not found"

search = input("Who to find: ")
print(linear_search(search,names))

