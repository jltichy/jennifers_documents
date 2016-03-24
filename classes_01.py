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

class Character(object):
    def_init_(self):
    self.health = 100
        
class Blacksmith(Character):
    def_init_(self):
    super(Blacksmith, self)._init_()
        

