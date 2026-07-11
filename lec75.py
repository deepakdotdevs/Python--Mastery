# Hybrid & Hierarchical Inheritance in python 

# Hybrid Inheritance in Python

# Hybrid inheritance is a combination of multiple inheritance and
# single inheritance in object-oriented programming. It is a type
# of inheritance in which multiple inheritance is used to inherit the
# properties of multiple base classes into a single derived class,
# and single inheritance is used to inherit the properties of the
# derived class into a sub-derived class.

# In Python, hybrid inheritance can be implemented by creating a
# class hierarchy, in which a base class is inherited by multiple
# derived classes, and one of the derived classes is further
# inherited by a sub-derived class.
    
# Hierarchical Inheritance

# Hierarchical Inheritance is a type of inheritance in Object-
# Oriented Programming where multiple subclasses inherit from a
# single base class. In other words, a single base class acts as a
# parent class for multiple subclasses. This is a way of
# establishing relationships between classes in a hierarchical
# manner.

# ---------------------------------------------------------------------------------

# Hybrid Example : 

# class BaseClass:
#     pass 
# class Derived1(BaseClass):
#     pass 
# class Derived2(BaseClass):
#     pass 
# class Derived3(Derived1, Derived2):
#     pass 


# Hierarchical Inheritence Example : 

class BaseClass:
    pass
class D1(BaseClass):
    pass 
class D2(BaseClass):
    pass 
class D3(D1):
    pass 