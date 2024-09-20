print ('***************************************\n
My Coffee and Muffin Shop\n
Number of coffees bought?')

numberCoffees = input ()

#Combines two steps by printing something while asking for an input
numberMuffins = input ('Number of muffins bought?')

#Goal is to prevent ordering one coffees or two coffee
if numberCoffees == 1:
  pluralCoffee = "s"
else
  pluralCoffee = ""

if numberMuffins == 1:
  pluralMuffin = "s"
else
  pluralMuffin = ""

#Total price to pay
coffeeCost = numberCoffees * 5
muffinCost = numberMuffins * 5
subtotal = coffeeCost + muffinCost
tax = subtotal * 0.06
total = subtotal + tax

print ('***************************************\n
***************************************\n
My Coffee and Muffin Shop Receipt\n'
numberCoffees + ' Coffee' + pluralCoffee + ' at $5 each: $ ' + coffeeCost + '\n'
numberMuffins + ' Muffin' + pluralMuffin + ' at $4 each: $ ' + muffinCost + '\n'
'6% tax: $ ' + tax + '\n
--------- \n
Total: $ ' + total + '\n
***************************************\n
Have a great day!\n
\n
***************************************')
