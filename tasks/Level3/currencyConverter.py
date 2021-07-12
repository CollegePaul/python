# conversion values
dollar = 1.28
euro = 1.10
currency = dollar

def convert_to():
  while True:
    convert = input("Do you want D - Dollars, or E - Euro")
    if convert=="D" or convert =="d":
      return dollar
    elif convert=="E" or convert == "e":
      return euro
    else:
      print("you need to enter E or D")

while True:
  #make a loop so the programm restarts
  loop = True
  while loop:
    #enter the amount of money and validate the input
    pounds = input("How much money in Pounds would you like to convert?")
    try:
        pounds = float(pounds)
        loop = False
    except ValueError:
        print("Sorry, that's not a valid amount of money")

  currency = convert_to()

  #perform caluculations
  output = pounds * currency

  if currency == dollar:
    print (f'£{pounds} is ${output:.2f}')
  else:
    print (f'£{pounds} is €{output:.2f}')
      
  

 