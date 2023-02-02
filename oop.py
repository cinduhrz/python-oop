##################################
## Object Oriented Programming
## Object
## -- described (properties, things the object IS)
## -- actions (methods, things the object can DO)
##################################

# Creating a Class
class Person:
    # name = "Alex"
    # age = 37
    
    # all functions in classes must be passed self
    # the object you're creating is always the first argument
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
# Class Inheritance
class Teacher(Person):
    
    def teach(self):
        print(f"{self.name} teaches")
        
    def smile(self):
        print(f"{self.name} smiles")
        
# Instantiating
# this is a (proper) OBJECT in python, so you CAN use dot notation here
# this is NOT a dictionary
alex = Teacher("Alex", 37)

print(alex.name, alex.age)
alex.teach()

class Dog:
    ## static variables
    ## outside the constructor
    
    # is a property of the class itself, not the instantiated objects
    # accessed like this: Dog.count
    count = 0
    
    
    # classmethod
    # @ indicates that this function works a lil diff
    # the entire Dog class is passed to this method
    @classmethod
    def one_more_dog(cls):
        cls.count += 1
    
    
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed
        Dog.one_more_dog() # this function belongs to the entire class (Dog), not to self
        
    def bark(self):
        print(f"{self.name} barks")
        
class SmallDog(Dog):
    
    ## overwriting (writing a version of a function that takes priority in a child class)
    def __init__(self, name, age, breed, sweater_color):
        ## call parent constructor so u dont have to write redundant stuff again
        ## keeps code DRY
        super().__init__(name, age, breed)
        self.sweater_color = sweater_color
        
    def bark(self):
        print(f"{self.name} yaps")

sparky = SmallDog("Sparky", 4, "Pug", "Orange")
biff = SmallDog("Biff", 5, "Pug", "Pink")
print(Dog.count)

print (sparky) # prints object at memory address
print(sparky.name, sparky.age, sparky.breed, sparky.sweater_color)
sparky.bark()

class Calculator:
    lastResult = 0
    
    @classmethod
    def calculate(cls, num1, num2, operator):
        # eval() takes a string and evaluates it as code
        # NEVER use it in prod
        # bc if you eval user input for example, you will run whatever the user puts in
        # so users can mess with your code
        # makes things easier but a lot less secure
        cls.lastResult = eval(f"{num1} {operator} {num2}")
        return cls.lastResult
        
        # static method
        # a pure function that has no access to any instance
        # doesnt need to talk self as arg
    @staticmethod
    def showLastResult():
        print(Calculator.lastResult)
            
Calculator.calculate(2, 2, "+")
Calculator.showLastResult()