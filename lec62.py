# Key Points -> Instance variable and Class variables in python 

# ------------------------------------------------------------------------------\\

# Instance vs class variables

# In Python, variables can be defined at the class level or at the instance
# level. Understanding the difference between these types of variables is
# crucial for writing efficient and maintainable code.

# Class Variables

# Class variables are defined at the class level and are shared among all
# instances of the class. They are defined outside of any method and are
# usually used to store information that is common to all instances of the
# class. For example, a class variable can be used to store the number of
# instances of a class that have been created.

# Instance Variables 

# Instance variables are defined at the instance level and are
# unique to each instance of the clas's. They are defined inside
# the init method and are usually used to store information that
# is specific to each instance of the class. For example, an
# instance variable can be used to store the name of an
# employee in a class that represents an employee.
# ------------------------------------------------------------------------------\\

# Instance Variable associated with Instance not the class
class Employee:
    companyName = "Apple"
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1
    def showDetails(self): # if we remove self, then error is this -> takes 0 positional arguments but 1 was given as emp1 argument is passes threw it
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Deepak")
emp1.showDetails() # or Employee.showDetails(emp1) both work is exactly same
# Employee.showDetails(emp1)
emp1.raise_amount = 0.3 # as it associated with the instance or object
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Ravi")
emp2.companyName = "Nestle"
emp2.showDetails()
