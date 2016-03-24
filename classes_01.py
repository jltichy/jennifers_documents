#!/usr/bin/env python

class BaseClass(object): # creating a class called base class that is inheriting from an object.
    def printHam(self):
        print 'Ham'

class InheritingClass(BaseClass): # creating an inheriting class that will inherit from the base class
    pass

x = InheritingClass() # creating an instance from the inheriting class
x.printHam() # accessing the function created within the base class

# the above program prints the word "Ham" to the screen

# what happens if we don't include the object in line 3? Note that BaseClass was changed to BC and InheritingClass was changed to IC for the sake of this example.

class BC: # creating a class called base class that is inheriting from an object.
    def printHam(self):
        print 'Ham'

class IC(BC): # creating an inheriting class that will inherit from the base class
    pass

x = IC() # creating an instance from the inheriting class
x.printHam() # accessing the function created within the base class

# the program still compiles properly but we're not actually accessing any variables or attributes

# Good practice - always include the object!
# Here's why OOP is cool - If you change the base class, it will affect all of the other inherited classes, with one easy step.

# Another example - with a character class:

class Character(object): # create a simple class
    def __init__(self): # calls the constructor self - notice that there is a space after def and that there are two underscores on either side of init
        self.health = 100 # create an attribute called health
        
class Blacksmith(Character): # creating inheriting class
    def __init__(self): # inherit from base class above
        super(Blacksmith, self).__init__() # super

bs = Blacksmith()
print bs.health

# the above program prints "100" to the screen

# if we delete the object from this example, the we do get an error because the super function no longer works.


# Yet another example - with an additional parameter:

class Char(object): # create a simple class; Character was shortened to Char for this example
    def __init__(self, name): # added the parameter called name
        self.health = 100 # create an attribute called health
        self.name = name # securing "name" to the class
    def PrintName(self):
        print self.name
        
class Black(Char): # creating inheriting class; Blacksmith was shortened to Black for this example
    def __init__(self, name, forgeName): # inherit from base class above
        super(Black, self).__init__(name) # super
        self.forge = Forge(forgeName)
        
class Forge:
    def __init__(self, forgeName):
        self.name = forgeName
    
BS = Black("Bob", "Rick\'s forge")
BS.PrintName()
print BS.forge.name