# Code by Kimball English
# Written on 12/4/2024
# Allows you to write code to a txt file
import csv
import math

grade1 = ''
grade2 = ''
grade3 = ''
firstName = ''
secondName = ''
getMoreNames = True
responceLoop = True

def writeMe (msg, document):
    csv.writer(document).writerow(msg)

def fCeil (x):
    return math.ceil(float(x))

def fFloor (x):
    return math.floor(float(x))

def getBothNames():
    while True:
        print('Please input the first name')
        name = input()
        try:
            name = float(name)
            print('The name cannot be a number')
        except:
            if len(name.strip()) == 0:
                print('The name cannot be blank')
            else:
                firstName = name
                break
    while True:
        print('Please input the second name')
        name = input()
        try:
            name = float(name)
            print('The name cannot be a number')
        except:
            if len(name.strip()) == 0:
                print('The name cannot be blank')
            else:
                secondName = name
                break
    return f'{firstName}-1{secondName}'
            
def getThreeGrades():
    while True:
        print('Please input the first grade')
        grade = input()
        try:
            if float(grade) >= 0 and fCeil(grade) == fFloor(grade):
                grade1 = grade
                break
            else:
                print('''The grade must be zero or greater and a whole
                      number''')
        except:
            print('The grade must be a whole number')
    while True:
        print('Please input the second grade')
        grade = input()
        try:
            if float(grade) >= 0 and fCeil(grade) == fFloor(grade):
                grade2 = grade
                break
            else:
                print('''The grade must be zero or greater and a whole
                    number''')
        except:
            print('The grade must be a whole number')
    while True:
        print('Please input the third grade')
        grade = input()
        try:
            if float(grade) >= 0 and fCeil(grade) == fFloor(grade):
                grade3 = grade
                break
            else:
                print('''The grade must be zero or greater and a whole
                    number''')
        except:
            print('The grade must be a whole number')
    return f'{grade1}-1{grade2}-1{grade3}'

# Basically my mian function

with open('grades.csv', mode='w', newline='') as document:
    while getMoreNames:
        responceLoop = True
        name = getBothNames()
        grade = getThreeGrades()
        grade1 = grade.split('-1')[0]
        grade2 = grade.split('-1')[1]
        grade3 = grade.split('-1')[2]
        firstName = name.split('-1')[0]
        secondName = name.split('-1')[1]
        # Just made writeMe bescause this was too long
        writeMe([firstName,secondName,grade1,grade2,grade3], document)
        while responceLoop:
            print('Do you want to add another person? (y/n)')
            responce = input()
            if responce == 'y':
                responceLoop = False
            elif responce == 'n':
                responceLoop = False
                getMoreNames = False
            else:
                print ('You must respond with y or n')
                
        
    
