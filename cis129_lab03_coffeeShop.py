print ('***************************************\n'
'My Coffee and Muffin Shop\n'
'Number of coffees bought?')

numberCoffees = input ()

print ('Number of muffins bought?')

numberMuffins = input ()

print ('Number of bagels bought?')

numberBagels = input ()

print ('Number of bananas bought?')

numberBananas = input ()

#Convert to int, so that it actually likes math
numberCoffees = int(numberCoffees)
numberMuffins = int(numberMuffins)
numberBagels = int(numberBagels)
numberBananas = int(numberBananas)

#Goal is to prevent ordering one coffees or two coffee
if numberCoffees == 1:
  pluralCoffee = ""
else:
  pluralCoffee = "s"

if numberMuffins == 1:
  pluralMuffin = ""
else:
  pluralMuffin = "s"

if numberBagels == 1:
  pluralBagel = ""
else:
  pluralBagel = "s"

if numberBananas == 1:
  pluralBanana = ""
else:
  pluralBanana = "s"

#Total price to pay
coffeeCost = numberCoffees * 5
muffinCost = numberMuffins * 4
bagelCost = numberBagels * 3
bananaCost = numberBananas * 6
subtotal = coffeeCost + muffinCost + bagelCost + bananaCost
tax = subtotal * 6 / 100
total = subtotal + tax

print ('***************************************\n'
 + '***************************************\n'
 + 'My Coffee and Muffin Shop Receipt\n'
 + str(numberCoffees) + ' Coffee' + pluralCoffee
+ ' at $5 each: $ ' + str(coffeeCost) + '\n'
 + str(numberMuffins) + ' Muffin' + pluralMuffin
+ ' at $4 each: $ ' + str(muffinCost) + '\n'
 + str(numberBagels) + ' Bagel' + pluralBagel
+ ' at $3 each: $ ' + str(bagelCost) + '\n'
 + str(numberBananas) + ' Banana' + pluralBanana
+ ' at $6 each: $ ' + str(bananaCost) + '\n'
 + '6% tax: $ ' + str(tax) + '\n'
 + '--------- \n'
 + 'Total: $ ' + str(total) + '\n'
 + '***************************************\n'
 + 'Have a great day!\n'
 + '\n'
 + '***************************************')
