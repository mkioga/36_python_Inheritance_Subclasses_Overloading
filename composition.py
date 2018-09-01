

# ===================================================
# Composition
# ===================================================

# Previously, we looked at polymorphism and saw how different objects can inherit similar behavior from a common basic class
# Hence although integer, string and tuples are different methods, they can all be printed because they all inherit
# the __str__ method from base "object" class
# Hence python is not interested on what things are, but how they behave

# We finished the last video by giving the Penguin class the same methods as the Duck class
# So penguin will behave the same as duck.
# And inheritance is not the only way to implement polymorphism.
# A class can behave the same way as another class as long as it has the necessary methods and data attributes

# Relating to Enemy class, we can say that a Troll "is an enemy" and a Vampire "is an enemny".
# So inheritance results in a "is a" relationship

# Now we will start looking at two other object orientated term, "Composition" and "Aggregation".
# "Composition" and "Aggregation" terms are used when you have a "Has a" relationship rather than a "is a" relationship.
# So if for example you are comparing a duck and wing, you say a "Duck has wings", hence composition/aggregation
# and not a "Duck is a wing" which would be inheritance.
# So use "is a" and "Has a" to test when to use "Inheritance", "Composition" and "Aggregation".



# =================================
# Ducks Class with composition
# =================================

# We will create a Wing Class here, and then give our Duck class below some Wings

class Wing(object):

    # define constructor
    def __init__(self, ratio):  # Add ratio to represent ratio of wing torgue to weight or Duck
        self.ratio = ratio

    # We define fly method define ease of flying by ratio of wing torgue by Duck weight
    def fly(self):
        if self.ratio > 1:
            print("Flying is Easy: Duck_weight / Wing_Torgue > 1")
        elif self.ratio == 1:
            print("Flying is hard: Duck_weight / Wing_Torgue = 1")
        else:
            print("Cannot Fly: Duck_weight / Wing_Torgue < 1")


# This is the Duck Class

class Duck(object):

    # Now we add a constructor to Duck object
    # And assign it "_wing" attribute of the "Duck" class
    # So any "Duck" object we create will have their own "_wing" object that can use the attributes of "Wing" e.g. fly methid
    # We give the self._wing for Duck a value of 1.8, which is the ratio of Duck_weight / Wing_torgue

    # "Composition" is When a class contains another object like here where "Duck" Class contains "Wing" class or object
    # So we can say that "Duck" has "Wing", or "Duck" is composed of "Wing" among other things, hence "Composition"
    # We can add other components that comprise a Duck e.g. "Beak" class, "Feet" class etc

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Duck Walking")

    def swim(self):
        print("Duck Swimming")

    def quack(self):
        print("Duck Quacking")

    # Then here we give the Duck a "fly" method
    # NOTE above "self._wing = Wing(1.8)" meaniing self._wing is assigned Wing(1.8) with parameter 1.8
    # Hence "self._wing.fly()" is same as "Wing.fly" method under Wing class and it has ratio 1.8
    # So the result here will be "Flying is Easy: Duck_weight / Wing_Torgue > 1"
    # NOTE: we will have to add test code under test instance "duck1" below

    def fly(self):
        self._wing.fly()


# Now we will create a Penguin class below
# NOTE that the penguin is not a duck, but it has the same "walk", "swim" and "quack" methods as a duck
# So we can do exactly the same thing with a duck as with a penguin

class Penguin(object):

    def walk(self):
        print("Penguin Walking")

    def swim(self):
        print("Penguin Swimming")

    def quack(self):
        print("Penguin Quacking")


# Now we will create a new Duck instance and see how it behaves
# NOTE: we may need to import our ducks into another module, so we make sure the main code does not run if ducks is imported.

if __name__ == '__main__':  # to make sure main code is not run if duck is imported
    duck1 = Duck()          # donald is a Duck object
    duck1.fly()             # We add a fly method to duck1 to test it

# When you run above code, you get result "Flying is Easy: Duck_weight / Wing_Torgue > 1"
# because we have ratio of 1.8 which is > 1

# Above is one way of demonstrating Composition
# We will create a new "html_doc.py" file to show how composition can be used in generating html code
