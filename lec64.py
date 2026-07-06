# Key Points -> class methods in python : 

# -----------------------------------------------------------

# Class methods are useful in several situations. For example,
# you might want to create a factory method that creates
# instances of your class in a specific way. You could define a
# class method that creates the instance and returns it to the
# caller. Another common use case is to provide alternative
# constructors for your class. This can be useful if you want to
# create instances of your class in multiple ways, but still have
# a consistent interface for doing so.

# How to Use Python Class Methods

# To define a class method, you simply use the
# "@classmethod" decorator before the method definition. The
# first argument of the method should always be "cls," which
# represents the class itself. Here is an example of how to
# define a class method:

# -----------------------------------------------------------

class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
e1 = Employee()
e1.name = "Deepak"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
