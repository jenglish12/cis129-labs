#Code by Kimball English
#Written on 12/4/2024
#Code to read a grades.txt file
megaValue = 0
sumOfParts = 0
isEmpty = False

with open('grades.txt', mode='r') as grades:
    for line in grades:
        for multiList in line.split('-1'):
            sumOfParts = 0
            isEmpty = False
            if multiList != '':
                #Gets fromating the way I want it
                print('\n\n\nName')
                print('   ' + multiList.split(',  ')[0] + '\n')
                print('Grades')
                try:
                    for part in multiList.split(',  ')[1].split(', '):
                        part = float(part)
                        print('   ' + f'{part:.2f}')
                except:
                    print('   None')
                    isEmpty = True
                #Next Value
                print('')
                print('Total')
                if isEmpty == False:
                    for part in multiList.split(',  ')[1].split(', '):
                        sumOfParts += float(part)
                    print('   ' + f'{sumOfParts:.2f}')    
                else:
                    print('   None')
                #Next Value
                print('')
                print('Count')
                if isEmpty == False:
                    print('   ' + f"""{len(multiList.split(',  ')[1].split(', ')
                        ):.2f}""")
                else:
                    print('   None')
                #Next Value
                print('')
                print('Average')
                if isEmpty == False:
                    average = sumOfParts/len(multiList.split(',  ')
                        [1].split(', '))
                    average = f'''{sumOfParts/len(multiList.split(',  ')
                        [1].split(', ')):.2f}'''
                    print('   ' + average)
                else:
                    print('   None')
