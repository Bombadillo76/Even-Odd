#Ask the user for a number. 
#Depending on whether the number is even or odd, 
#print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when divided by 2?

number = input("Please enter an integer (a whole number or its opposite - no decimals, please): ")
number = float(number)
if number%2 == 0:
  print("Your number is even.")
elif number%2 == 1:
  print("Your number is odd.")
else:
  print("Ok, wise guy, please try to follow the rules.")