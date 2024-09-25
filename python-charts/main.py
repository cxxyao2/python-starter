
from typing import Self

# Python Syntax Basics
def our_function():
    print("Hello from our function")
    print("Hello again")

our_function()

# Python Variables
single_line_string = 'This is a single line string'
print(single_line_string)

multi_line_string='''This is a multi line string using
Realy cool strip 
 triple quotes.'''
print(multi_line_string)    

#Long Statements
if(1 < 2) and (2 < 3) and \
(3 < 4) and (4 < 5):
    print("Multi-line statement is running")


# Casing

# snake_case
python_syntax= "Snake case is used for variable names, function names, and module names."
PYTHON_CONS = "Python constants are usually written in all uppercase letters with underscores separating words."

class Car:
    def __init__(self, color: str, horsepower: int) -> None:
        self.color = color
        self.horsepower = horsepower
    
    def drive(self) -> None:
        print(f"The car is driving with {self.horsepower} horsepower")

    def get_info(self,var) -> None:
        print(var)
        print(f"The car is {self.color} and has {self.horsepower} horsepower")

    def __str__(self) -> str:
        return f"The car is {self.color} , {self.horsepower} horsepower"
    
    def __add__(self,other:Self) -> str:
        return f"New model is combined from'{self.brand}'& {other.brand})"    

volvo:Car = Car("red", 300)
print(volvo.color)
volvo.drive()
volvo.get_info("volvo")

bmw:Car = Car("blue", 200)
print(bmw.color)
bmw.drive()
bmw.get_info("bmw")
print(bmw)

p