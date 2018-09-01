
# =================================
# enemy.py
# =================================

# =================================
# superclasss Enemy
# =================================


# This superclass enemy has the defined properties
# and any enemy object that is created from this superclass will have the same properties
# This enemy class will be called in the main.py class

# NOTE that this Enemy superclass is itself a subclass of built in class called "Object"
# Because every class ultimately inherits from a class "Object"
# In python 2 and below, we would have used "class Enemy(Object):" instead of just "class Enemy"

# We use "class Enemy" in python 3 because each class in python 3 ultimately inherits from class object
# And if we have a class with no superclass, it will automatically inherit from class "object"

# class Enemy(object):  # python 2 and below

class Enemy:  # python 3

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False

    def __str__(self):
        return("Name: {0.name}, Hit Points: {0.hit_points}, Lives: {0.lives}".format(self))


# =====================================================================
# Troll - Subclass with no parameters inheriting superclass parameters
# =====================================================================

# We will create an enemy instance called Troll who will inherit Enemy characteristics
# "Troll" is a subclass of "Enemy" and is defined as follows

# NOTE: In this case, we will not put any code under class, but will use "pass" so that there is no python error
# "pass" does nothing but is seen by python as a code
# for more on "pass", type "pass in python 3" on google.

class Troll(Enemy):
    pass



# ========================================================
# Troll2 - subclass with parameters inheriting superclass
# ========================================================

# subclass Troll2 has its own __init__ which we pass a "name" to it
# We also inherit superclass Enemy __init__ to retain its parameters
# NOTE that since we pass "name" to Troll2, we add name=name to Enemy__init__ name


class Troll2(Enemy):

    def __init__(self, name):
        Enemy.__init__(self, name=name, lives=1, hit_points=23)


# ====================================================
# Troll3 - Using "super" for inheritance
# ====================================================

# Another way to inherit superclass "Enemy's" parameters is to use keyword "super" as shown
# Here we are passing the name of our class (Troll3) and the current instance (self)
# to "super" and then we use that to call the __init__ method of the superclass "Enemy"

class Troll3(Enemy):

    def __init__(self, name):
        super(Troll3, self).__init__(name=name, lives=1, hit_points=23)


# ======================================================
# Troll4 - Shorter way to use "super"
# ======================================================

# This is a shorter way of using super
# we use super() instead of super(Troll3, self). Python compiler adds (Troll3, self) automatically
# This is the recommended method

class Troll4(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)



# =======================================================
# Troll5 - Adding more function to subclass
# =======================================================

# A Subclass can have more functionality than one in superclass
# In this case, we will add method "grunt" to Subclass "Troll5"


class Troll5(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("My name is {} and I will stomp you".format(self.name))



# ==============================================================
# Challenge - Vampire class
# ==============================================================

# Create a new vampire class that is a subclass of Enemy
# Vampires have 3 lives, and take 12 hitpoints of damage
# You can create a new python file for the vampire if you like but its better to add to existing enemy.py file

# Test your class by creating one or two Vampire instances and displaying their details
# Also inflict some damage to make sure the take_damage method works okay
# Also make sure the trolls can also take damage because we have not tested that so far



class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)


    # ==============================================================
    # Changing behavior of a subclass
    # ==============================================================

    # Here we will see how to change the behavior so that a subclass can implement a method
    # from its superclass and do things differently
    # In this case, we will change the take.damage method so that vampires can dodge when attacked.

    # we will introduce a random element so that a vampire has 1 in 3 chance of dodging a blow.
    # We will use the random module to generate a random number between 1 and 3 inclusive.
    # if we get a 3, the vampire successfully dodges the blow.


    def dodges(self):
        import random  # import randoom module. NOTE: This can also be imported at the top of the enemy.py file
        if random.randint(1, 3) == 3:  # if random number generated equals 3
            print("***** {0.name} dodges *****".format(self))
            return True  # The dodge is true
        else:
            return False  # Else the dodge is false i.e. it fails


    # ===========================================================
    # Overriding a method
    # ===========================================================

    # Overriding a method means replacing it with another one.
    # in python, we just write a new method with the same name as the one you want to override.
    # We will overide the Enemy classs take_damage method to make it do something different in the vampire class.

    # Here we create new method called "take_damage" which does nothing (pass)
    # This method will be used instead of the "take_damage" method from Enemy class above which actually reduces the lives

    # This is why this method results in a loop because in main.py, the vamp.take_damage(1) in while vamp.alive uses
    # This new method below which does nothing.
    # This just demonstrates that this new take_damage is going to be used instead of the one from Enemy that
    # it is overriding.

    # def take_damage(self, damage):
    #     pass


    # We will now use this new take_damage module and use it to check if Enemy dodges any damage (i.e. random got a 3)
    # So we don't have to test for that in the main.py program
    # If it does not dodge, we then take the "take_damage" from Enemy (using keyword super) and show the damage

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)




# ====================================
# Inheritance challenge - VampireKing
# ====================================

# Create VampireKing subclass of Vampire
# VampireKing is going to be very powerful, and any points of damage inflicted will be divided by 4
# VampireKing objects will also start off with 140 hit points

# "Extend" the Vampire class to create VampireKing class with those additional properties
# Then test the new class by creating a new VampireKing object and checking that it does start
# with 140 hit points and only takes a quarter of the damage inflicted.



class VampireKing(Vampire):  # we add Vampire because we are extending it from Vampire

    def __init__(self, name):  # We add the constructor and will pass it a name argument
        super().__init__(name=name)  # Then we get the Super __init__ constructor (super = Vampire's init) and pass name to it
        self.hit_points = 140       # This constructor is same as Vampire, hence we need to initialize the hit_points to 140

    # Now we call the take_damage method and integer divide it by 4
    # we use integer divide because we don't want to end up with fractional lives

    def take_damage(self, damage):
        super().take_damage(damage // 4)
