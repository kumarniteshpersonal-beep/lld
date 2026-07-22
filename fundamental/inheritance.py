# Inheritance basics
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.eat() # Output: Animal eats

# Multilevel Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    pass

class D(B, C):
    pass

# Python uses C3 linearization to determine the method resolution order (MRO) for classes in multiple inheritance scenarios. 
# It guarantees:
#     Child classes come before parents
#     Left-to-right inheritance order is preserved
#     Consistent ordering
#     No ambiguity
# The MRO is determined using the C3 algorithm, which ensures a consistent and predictable method resolution order while respecting the hierarchy of the classes.
print(D.mro())
D().show() # Output: B, because B is the first class in the MRO that defines the show method.