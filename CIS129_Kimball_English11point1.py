# Code by Kimball English
# Written on 12/4/2024
# Allows you to write code to a txt file

def getName():
    while True:
        print('Please input a name, -1 to quit')
        name = input()
        try:
            name = float(name)
            # Create exception for sentanal value
            if name == -1:
                return '-1'
            else:
                print('The name cannot be a number')
        except:
            if len(name.strip()) == 0:
                print('The name cannot be blank')
            else:
                return name
            
def getGrade():
    while True:
        print('Please input a grade, -1 to quit')
        grade = input()
        try:
            if float(grade) >= 0:
                return grade
            # Create exception for sentanal value
            elif float(grade) == -1:
                return '-1'
            else:
                print('The grade must be zero or greater')
        except:
            print('The grade must be a number')
            
gradeList = ""
with open('grades.txt', mode='w') as document:
    name = getName()
    while name != '-1':
        gradeList = ''
        grade = getGrade()
        while grade != '-1':
            if gradeList != "":
                gradeList = f'{gradeList}, {grade}'
            else:
                gradeList = grade
            grade = getGrade()
        str(gradeList)
        document.write(f'{name},  {gradeList}-1')
        name = getName()
