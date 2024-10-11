# Code by Kimball English
# Made 10/10/24
# This program calculates the number of bottles recycled and the payout that the
# machine would need to payout for those bottles

#initialize variables
total_bottles = 0
counter = 1 
today_bottles = 0 
total_payout = 0 
keep_going = 'y'  

while keep_going == 'y': #loops so you can input multiple weeks
    while counter < 8: #loops for all eight days
        today_bottles = int(input(f"Enter number of bottles for day #{counter}: ")) 
        total_bottles += today_bottles
        counter += 1 

    total_payout = total_bottles * 0.1 #Pays out a dime for each bottle
    print()
    print(f'The total number of bottles collected is {total_bottles}')
    print(f'The total paid out is $ {total_payout:.1f}')
    print()
    print("Do you want to enter another week’s worth of data?")
    if input('(Enter y or n): ') == 'n':
        keep_going = 'n' #Ends the program
    else:
        #Preps for next week by resetting variables
        counter = 1
        today_bottles = 0
        total_payout = 0
        total_bottles = 0
        print()
