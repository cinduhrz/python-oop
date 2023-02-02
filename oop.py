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
    
    
    def teach(self):
        print(f"{self.name} teaches")
        
# Instantiating
# this is a (proper) OBJECT in python, so you CAN use dot notation here
# this is NOT a dictionary
alex = Person("Amy", 37)

print(alex.name, alex.age)
alex.teach()