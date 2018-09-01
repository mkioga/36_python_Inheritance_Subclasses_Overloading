

# =====================================================
# main.py - Inheritance
# =====================================================



# This is where you have a superclass, and subclasses
# Subclasses inherit the characteristics of superclass

# we will create a superclass called "enemy.py"


# Now that the enemy.py superclass is created, we will make an instance of enemy to test it

print("="*40)
print("Calling enemy class:")
print("="*20)
print()
# first we import Enemy from enemy.py
# NOTE: we can import two classes at the same time as shown.  Here we import Enemy and Troll

from enemy import Enemy, Troll

# then we create an enemy instance called random_monster with characteristics of enemy
# we pass it name = basic enemy, hit_points = 12 and lives = 1

random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

# Then we give it damage of 4

print("="*20)
random_monster.take_damage(4)
print(random_monster)

# Now we take 8 points of damage to bring the hit_points to 0
# We still have 1 live left

print("="*20)
random_monster.take_damage(8)
print(random_monster)

# And then take another 4 points to bring the hit_points to -4
# After hit_points goes to -4, we now have 0 lives (1-1 = 0)

print("="*20)
random_monster.take_damage(4)
print(random_monster)


# ==========================================
# Now we call the subclass Troll
# ==========================================

# NOTE we imported Troll above

# We don't pass any parameters to ugly_troll hence it has default name "Enemy" Hit points = 0 and Lives = 1

print("="*40)
print("Calling Troll")
print()


print("="*20)
ugly_troll = Troll()
print("Ugly Troll = {}".format(ugly_troll))

# Now we create ugly_troll2 and pass it parameters
# this one prints the parameters we gave it. It overides the default parameters

print("="*20)
ugly_troll2 = Troll("Ugly_troll2", 18, 1)
print("Ugly Troll_2 = {}".format(ugly_troll2))


# We can also make another troll and pass it two parameters and it will take default live of 1

print("="*20)
ugly_troll3 = Troll("Ugly_troll3", 25)
print("Ugly Troll_2 = {}".format(ugly_troll3))

# ========================
# No overloading in python
# ========================
# in python, if you use same parameter twice e.g ugly_troll3. it will retain the last value that it got
# There is no concept of overloading in python like there is in java


print("="*20)
ugly_troll3 = Troll("Ugly_troll3", 50, 2)
print("Ugly Troll_2 = {}".format(ugly_troll3))


# =========================================================
# Now we will call subclass Troll2
# =========================================================

# we have to import Troll2
# And Troll2 takes only name parameter

from enemy import Troll2


print("="*40)
print("Calling Troll2")
print()

print("="*20)
ugly_troll = Troll2("Ugly_troll")
print("Ugly Troll = {}".format(ugly_troll))

print("="*20)
ugly_troll2 = Troll2("Ugly_troll2")
print("Ugly Troll_2 = {}".format(ugly_troll2))

print("="*20)
ugly_troll3 = Troll2("Ugly_troll3")
print("Ugly Troll_2 = {}".format(ugly_troll3))




# =========================================================
# Now we will call subclass Troll3
# =========================================================

# we have to import Troll3
# And Troll3 takes only name parameter

from enemy import Troll3


print("="*40)
print("Calling Troll3")
print()

print("="*20)
ugly_troll = Troll3("Ugly_troll")
print("Ugly Troll = {}".format(ugly_troll))

print("="*20)
ugly_troll2 = Troll3("Ugly_troll2")
print("Ugly Troll_2 = {}".format(ugly_troll2))

print("="*20)
ugly_troll3 = Troll3("Ugly_troll3")
print("Ugly Troll_2 = {}".format(ugly_troll3))





# =========================================================
# Now we will call subclass Troll4
# =========================================================

# we have to import Troll4
# And Troll3 takes only name parameter

from enemy import Troll4


print("="*40)
print("Calling Troll4")
print()

print("="*20)
ugly_troll = Troll4("Ugly_troll")
print("Ugly Troll = {}".format(ugly_troll))

print("="*20)
ugly_troll2 = Troll4("Ugly_troll2")
print("Ugly Troll_2 = {}".format(ugly_troll2))

print("="*20)
ugly_troll3 = Troll4("Ugly_troll3")
print("Ugly Troll_2 = {}".format(ugly_troll3))


# =========================================================
# Now we will call subclass Troll5
# =========================================================

from enemy import Troll5


print("="*40)
print("Calling Troll5 - grunt")
print()


print("="*20)
ugly_troll = Troll5("Ugly_troll")
ugly_troll.grunt()

print("="*20)
ugly_troll2 = Troll5("Ugly_troll2")
ugly_troll2.grunt()

print("="*20)
ugly_troll3 = Troll5("Ugly_troll3")
ugly_troll3.grunt()
ugly_troll3.take_damage(5)
print(ugly_troll3)

# ===============================================
# Test Vampire class
# ===============================================

# import vampire class

from enemy import Vampire

# Then we create an instance of Vampire and call Vampire class and pass it name (vamp_vlad)

print("="*20)
vamp = Vampire("Vamp_vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)


# # ================================================
# # We will use a while loop to test self.alive
# # ================================================
#
# print("="*20)
# while vamp.alive:
#     vamp.take_damage(1)
#     print(vamp)


# # ========================================================
# # We will test this to check if vamp dodges i.e. gets a 3
# # ========================================================
#
# print("="*20)
# while vamp.alive:
#     if not vamp.dodges():
#         vamp.take_damage(1)
#         print(vamp)


# ==========================================================
# Now we check the new take_damage module (using overriding)
# ==========================================================
# NOTE that now we don't have to test for vamp.dodges
# We see this now works and has no loop

# print("="*20)
# while vamp.alive:
#     vamp.take_damage(1)
#     print(vamp)


# ==============================================================
# Rrefactoring and Replacing - Modifying private attributes
# ==============================================================

# NOTE that you can access and modify the Enemy attributes here and modify them
# We are actually not supposed to access them like this.
# One way to indicate that the attributes should not be accessed is to name them starting with underscore (_)
# But this is just a convention and python does not enforce it.
# You can refactor them using Refactor > Rename

# NOTE that when refactoring, intellij may not change the names in named placement fields
# e.g. {0.name}, in enemy.py. so you may refactor and it will not rename these ones and you have to do it manually.

# One way to change the names of those in {0.name} is using ==> Edit > Find > Replace
# Under Replace box ===> (\{\d\.)  <<=== This will find anything matching {d. where d is any digit
# Under Replace with ==> $1_  <<==== which replaces . with ._
# Remember to check the box for Regex


vamp.lives = 0
vamp.hit_points = 1
print(vamp)


# ============================================
# Testing Inheritance challenge - VampireKing
# ============================================

# We will create an instance of VampireKing called Dracula

# first import VampireKing class from enemy.py

from enemy import VampireKing

# dracula is an instance of VampireKing class and we pass its name i.e. Dracula

print("="*20)
dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(40)  # we give it 40 points damage which will be divided by 4 to become 10
print(dracula)  # Result will be 130 points remaining, unless he dodges and avoids all damage


