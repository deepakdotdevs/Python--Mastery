# Key Points : super keyword in python 

# The super() keyword in Python is used to refer to the parent class. It is especially useful
# when a class inherits from multiple parent classes and you want to call a method from one
# of the parent classes.

# When a class inherits from a parent class, it can override or extend the methods defined in
# the parent class. However, sometimes you might want to use the parent class method in the
# child class. This is where the super0 keyword comes in handy.

# ----------------------------------------------------------------

# Program No. 1 : 

# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method")
# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Deepak")
#         super().parent_method()
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()
# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

# ----------------------------------------------------------------

# Program No. 2 : 

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
rohan = Employee("Rohan Das", 101)
deepak = Programmer("Deepak Jangid", 102, "Python")
print(deepak.name, deepak.id, deepak.lang)
