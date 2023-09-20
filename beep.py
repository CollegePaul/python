import winsound


# Frequency , time in miliseconds
#eg  from 500 hz to 4000hz in 250hz intervals for 300 ms  (0.3 seconds)

for x in range(500,4000,250):
    winsound.Beep(x, 300)

#this works