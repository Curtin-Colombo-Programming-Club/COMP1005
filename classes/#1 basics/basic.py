from typing import Self

# Define a basic class
class MyClass:
    # The initializer (also known as the constructor)
    # It is automatically called when an instance of the class is created
    def __init__(self) -> Self:
        # Initializing class attributes
        self.attr1: int = 1  # Integer attribute
        self.attr2: str = "abc"  # String attribute
        
        # Returning the instance of the class
        return self

    # Method that takes a value and compares it to attr2
    def someFunction(self, val) -> bool:
        # Using 'is' to check if the input is the same object as attr2
        return self.attr2 is val

    # Dunder (magic) method to return a string representation of the class
    def __str__(self) -> str:
        # Returning a formatted string of the class attributes
        return f"MyClass(attr1: {self.attr1}, attr2: {self.attr2})\n"

# Example usage:
# Creating an instance of MyClass
my_instance = MyClass()

# Printing the object, which uses the __str__ method
print(my_instance)  # Output: MyClass(attr1: 1, attr2: abc)

# Checking if 'abc' is the same object as attr2
print(my_instance.someFunction("abc"))  # Output: True


# Define another class with parameters in the constructor
class ParamClass:
    # The initializer with parameters to pass values at object creation
    def __init__(self, param1: int, param2: str) -> Self:
        # Initializing attributes with passed values
        self.attr1: int = param1  # Assign param1 to attr1
        self.attr2: str = param2  # Assign param2 to attr2
        
        # Returning the instance of the class
        return self

    # Method to compare attr2 with a passed value
    def someFunction(self, val) -> bool:
        # Using 'is' to check if val is the same object as attr2
        return self.attr2 is val

    # Dunder (magic) method to return a string representation of the class
    def __str__(self) -> str:
        # Returning a formatted string of the class attributes
        return f"ParamClass(attr1: {self.attr1}, attr2: {self.attr2})\n"

# Example usage:
# Creating an instance of ParamClass with custom parameters
param_instance = ParamClass(10, "xyz")

# Printing the object, which uses the __str__ method
print(param_instance)  # Output: ParamClass(attr1: 10, attr2: xyz)

# Checking if 'xyz' is the same object as attr2
print(param_instance.someFunction("xyz"))  # Output: True
