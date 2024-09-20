print ('***************************************\n'
'My Coffee and Muffin Shop\n'
'Number of coffees bought?')

numberCoffees = input ()

print ('Number of muffins bought?')

numberMuffins = input ()

#Convert to int, so that it actually likes math
numberCoffees = int(numberCoffees)
numberMuffins = int(numberMuffins)

#Goal is to prevent ordering one coffees or two coffee
if numberCoffees == 1:
  pluralCoffee = "s"
else:
  pluralCoffee = ""

if numberMuffins == 1:
  pluralMuffin = "s"
else:
  pluralMuffin = ""

#Total price to pay
coffeeCost = numberCoffees * 5
muffinCost = numberMuffins * 4
subtotal = coffeeCost + muffinCost
tax = subtotal * 6 / 100
total = subtotal + tax

print ('***************************************\n'
 + '***************************************\n'
 + 'My Coffee and Muffin Shop Receipt\n'
 + str(numberCoffees) + ' Coffee' + pluralCoffee
+ ' at $5 each: $ ' + str(coffeeCost) + '\n'
 + str(numberMuffins) + ' Muffin' + pluralMuffin
+ ' at $4 each: $ ' + str(muffinCost) + '\n'
 + '6% tax: $ ' + str(tax) + '\n'
 + '--------- \n'
 + 'Total: $ ' + str(total) + '\n'
 + '***************************************\n'
 + 'Have a great day!\n'
 + '\n'
 + '***************************************')
