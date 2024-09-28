# Module 4 Lab-4
# Kimball English
# 9/27/2024
# This program determains monthly bonus's for a store and its employees

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = "Enter" # prompt will be a string literal

    

# This code gets the monthly sales

monthlySales = float(input(prompt+ ' the monthly sales $'))

# This code determines the store bonus

if monthlySales > 110000: #The document said greater than, not greater than or
    #equal to. Might be a typo because I think this is the only case where this
    #happens.
	storeAmount = 6000
elif monthlySales >= 100000:
	storeAmount = 5000
elif monthlySales >= 90000:
	storeAmount = 4000
elif monthlySales >= 80000:
	storeAmount = 3000
#else:
	#______________________
#You dont need the else statment. We already set storeAmount to 0 when declaring
#it. The else would set it to 0 redundantly. 


# This code gets the percent of increase in sales
salesIncrease = float(input(prompt+ " percent of sales increase: "))
salesIncrease = salesIncrease / 100


# This code determines the employee bonus
if salesIncrease >= 0.05:
	empAmount = 75
elif salesIncrease >= 0.04:
	empAmount = 50
elif salesIncrease >= 0.03:
	empAmount = 40
#else:
#	empAmount = ____
#Also not needed. 
# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000 ) and (empAmount == 75):
	print('Congrats! You have reached the highest bonus amounts possible! ')

