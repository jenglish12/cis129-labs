# Programed by Kimball English
# Programed on 12/9/2024
# Program creates a custome pet class and makes an
# animal object of the pet class

class pet:
    def __init__(self, Name, Type, Age):
        self.Name = Name
        self.Type = Type
        self.Age = Age

    #Name methods

    def getName(self):
        return self._Name

    def setName(self, Name):
        if Name.strip() != '':
            self._Name = Name
        else:
            raise ValueError
        
    #Type methods
        
    def getType(self):
        return self._Type

    def setType(self, Type):
        if Type.strip() != '':
            self._Type = Type
        else:
            raise ValueError
    #Age methods
                    
    def getAge(self):
        return self._Age

    def setAge(self, Age):
        try:
            int(Age)
            if int(Age) > 0:
                self._Age = Age
            else:
                raise ValueError
        except:
            raise ValueError
        

def main ():

    inputName = ''
    inputType = ''
    inputAge = 0

    #Need temp variable to create the Animal
    Animal = pet('','',-1)

    #Validation loops to prevent errors
    while True:
        try:
            print('Enter a pet name:')
            Animal.setName(input())
            break
        except:
            print('Name cannot be blank')
            
    while True:
        try:
            print('Enter a pet type:')
            Animal.setType(input())
            break
        except:
            print('Type cannot be blank')
            
    while True:
        try:
            print('Enter a pet age:')
            Animal.setAge(input())
            break
        except:
            print('Age must be a whole number greater than zero')

    print('The pet name is', str(Animal.getName()))
    print('The pet type is', str(Animal.getType()))
    print('The pet age is', str(Animal.getAge()))

main()
