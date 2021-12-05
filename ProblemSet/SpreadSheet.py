#ascii for A = 65

#this will convert spreadsheet columns into decimal values

s = input("Enter your string: ")
total = 0

for i in range(len(s)):
  total += ((ord(s[i])-64) * pow(26,len(s)-1-i))

print (total)


#DHL = 2924
