
# =======================================
# Polymorphism
# =======================================

# We have three variables, integer, string and tuple.
# When we print them, it prints fine.

# What happened is we have passed three different variables (integer, string, tuple) to the print function
# and it has printed a value for each one of them

# So what happened here is that each object is behaving in a similar way when we try to print it.
# In addition their behavior as an integer, string or tuple, they also have a printable behavior

# a is an integer and b is a string.
# you can subtract an integer from another integer, but cannot subtract a string from another (hence int and string are different objects)

# But a and b also share a printable behavior,
# and in that respect, behave like a different type of object; an object that is printable.

# Polymorphism is the ability of objects to have different forms, e.g. be an integer and be printable.
# This also means they have many forms.
# Poly (means many) Morphe (means form)

a = 3
b = "Dylan"
c  = 1, 2, 3

print(a)
print(b)
print(c)
print("="*20)

# In above example, the polymorphic behavior of the objects is implemented using inheritance.
# All python objects inherit from a base class called "object", which defines a __str__ method
# So polymorphism allows the print function to accept arguments of any type, and its able to print them out.

# Python is able to print different types of objects by delegating the printing to another _str__ class that would be
# able to print different objects.

# One way to implement Polymorphism is by using inheritance
# For example, int and string have their own characteristics, but they can both be printed.
# The printed characteristic in both int and string is possible because every object inherits the __str__ method
# from its object base class. And so it inherits its printable characteristic from __str__ method.

# So the print function in python can be used on any object because every object inherits __str__ method from the object base class

# We will create a Ducks class below to show how polymorphism works in python

# =========================
# Inheritance
# =========================

# ===============================
# Ducks Class with inheritance
# ===============================

# We will create a duck object with the following characteristics

class Duck(object):

    def walk(self):
        print("Duck Walking")

    def swim(self):
        print("Duck Swimming")

    def quack(self):
        print("Duck Quacking")



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


# Now we will create a function to test our duck class.
# This test_duck function takes a single argument and calls its walk, swim and quack methods

def test_duck(duck_instance):  # we pass test_duck a duck a duck_instance
    duck_instance.walk()
    duck_instance.swim()
    duck_instance.quack()

# Now we will create a new Duck instance and see how it behaves
# NOTE: we may need to import our ducks into another module, so we make sure the main code does not run if ducks is imported.

if __name__ == '__main__':  # to make sure main code is not run if duck is imported
    duck1 = Duck()         # donald is a Duck object
    test_duck(duck1)       # We pass donald as a duck instance to test_duck

    # Now we will create a penguin class and test it
    # Although we know that Penguin is not a duck, it has same characteristics and hence Penguin can be passed to test_duck
    # and still create valid results.
    # So python does not mind what a class is, but how it behaves. If it has characteristics that a function is looking for, then it will work

    # This is similar to polymorphism for print function where all objects inherit __str__ method from base "object" and hence can be printed

    print("="*20)
    penguin1 = Penguin()  # penguin1 is an instance of Penguin class
    test_duck(penguin1)   # We use test_duck to print the walk, swim, quack methods because they are same for Duck and Penguin



# Duck test in wikipedia - if it looks like a duck, swims like a duck, quacks like a duck, then its probably a duck
# this approach is fundamental to the way python deals with objects.
# Unlike "Static" typed languages, that require the type of every object to be declared when it is used,
# Python "Dynamic" typing means its only interested in what can be done with an object.
# If an object has the necessary attributes, then python is quite happy for it to be used.
# So this phrase "duck typed" is commonly used in dynamically typed languages

