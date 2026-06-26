# Key Points : Access Modifiers in Python : 

# Access specifiers or access modifiers in python programming are used to
# limit the access of class variables and class methods outside of class while
# implementing the concepts of inheritance.

# Let us see the each one of access specifiers in detail:

# Types of access specifiers

# 1. Public access modifier
# 2. Private access modifier
# 3. Protected access modifier

# ----------------------------------------------------------------------------

# There are no Access Modifiers in Python by Default.

# ----------------------------------------------------------------------------

# # Public access Specifier in python : by default public 

# # All the variables and methods (member functions) in python are by default
# # public. Any instance variable in a class followed by the 'self' keyword ie.
# # self.var_name are public accessed.

# # Program/Example :

# # class Employee:
# #     def __init__(self):
# #         self.name = "Deepak"
# # a = Employee()
# # print(a.name) # name is publicily accessible as we access it easily (by default public)

# # Program/Example 2 : 

# class Student:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
# obj = Student("Deepak", 21)
# print(obj.age)
# print(obj.name)

# ----------------------------------------------------------------------------

# # Private access Specifier in python :

# By definition, Private members of a class (variables or methods) are those
# members which are only accessible inside the class. We cannot use
# private members outside of class.

# In Python, there is no strict concept of "private" access modifiers like in
# some other programming languages. However, a convention has been
# established to indicate that a variable or method should be considered
# private by prefixing its name with a double underscore (_). This is known
# as a "weak internal use indicator" and it is a convention only, not a strict
# rule. Code outside the class can stillaccess these "private" variables and
# methods, but it is generally understood that they should not be accessed
# or modified.

# Program/Example : 

# class Employee:
#     def __init__(self):
#         self.__name = "Deepak"
# a = Employee()
# # print(a.__name) # We can't access it

# # But by this, we can access it
# print(a._Employee__name) # worked

# print(a.__dir__()) # shows all the methods, functions we can perform on a

# ----------------------------------------------------------------------------

# Name mangling : 

# Name mangling in Python is a technique used to protect class-private and
# superclass-private attributes from being accidentally overwritten by
# subclasses. Names of class-private and superclass-private attributes are
# transformed by the addition of a single leading underscore and a double
# leading underscore respectively.

# example program :

# class myClass:
#     def __init__(self):
#         self._private_attribute = "I'm a private attribute"
#         self.__mangled_attribute = "I'm a mangled attribute"
# myObj = myClass()
# print(myObj._private_attribute)
# print(myObj.__mangled_attribute)
# print(myObj._myClass__mangled_attribute)

# ----------------------------------------------------------------------------

# Protected Access Modifier :

# In object-oriented programming (OOP), the term "protected" is
# used to describe a member (i.e., a method or attribute) of a class
# that is intended to be accessed only by the class itself and its
# subclasses. In Python, the convention for indicating that a
# member is protected is to prefix its name with a single
# underscore (). For example, if a class has a method called
# _my_method, N is indicating that the method should only be
# accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming
# convention, and does not actually provide any protection or
# restrict access to the member. The syntax we follow to make any
# variable protected is to write variable name followed by a single
# underscore () ie. _varName.

class Student:
    def __init__(self):
        self._name = "Deepak"
    def _funName(self):
        return "Diaries of Deepak" # protected method
class Subject(Student):
    pass
obj = Student()
obj1 = Subject()
print(dir(obj)) # all operation we can perform on, there is no mangling
# calling by object of student class
print(obj._name)
print(obj._funName())
# calling by object of subject class
print(obj1._name)
print(obj1._funName())
