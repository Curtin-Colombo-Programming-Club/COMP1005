from typing import Self

# Define a class 'Animal' with attributes and methods
class Animal:
    # The initializer (constructor) to set up initial attributes
    def __init__(self, name: str, age: int, gender: str):
        self.name: str = name  # String attribute to store the animal's name
        self.age: int = age    # Integer attribute to store the animal's age
        self.gender: str = gender  # String attribute to store the animal's gender

    # Accessor methods (getters) to retrieve the values of attributes

    def getName(self) -> str:
        """
        Accessor method for 'name'.
        Returns the name of the animal.
        """
        return self.name

    def getAge(self) -> int:
        """
        Accessor method for 'age'.
        Returns the age of the animal.
        """
        return self.age
    
    def getGender(self) -> str:
        """
        Accessor method for 'gender'.
        Returns the gender of the animal.
        """
        return self.gender

    # Mutator methods (setters) to modify the values of attributes

    def setName(self, new_name: str) -> Self:
        """
        Mutator method for 'name'.
        Sets a new value for the name.
        Returns the object instance for method chaining.
        """
        self.name = new_name
        return self

    def setAge(self, new_age: int) -> Self:
        """
        Mutator method for 'age'.
        Sets a new value for age if it's in the valid range (0-99).
        Returns the object instance for method chaining.
        """
        if new_age in range(0, 100):  # Ensures age is in a valid range
            self.age = new_age
        return self

    def incrAge(self) -> Self:
        """
        Mutator method to increment the age by 1.
        Returns the object instance for method chaining.
        """
        self.age += 1
        return self


# Example usage:

# Create an instance of the Animal class
animal1 = Animal("Lion", 5, "Male")

# Access attributes using accessor methods (getters)
print(f"Name: {animal1.getName()}")   # Output: Name: Lion
print(f"Age: {animal1.getAge()}")     # Output: Age: 5
print(f"Gender: {animal1.getGender()}")  # Output: Gender: Male

# Modify attributes using mutator methods (setters)
animal1.setName("Tiger").setAge(7)  # Chaining mutator methods
print(f"Updated Name: {animal1.getName()}")  # Output: Updated Name: Tiger
print(f"Updated Age: {animal1.getAge()}")    # Output: Updated Age: 7

# Increment age using incrAge method
animal1.incrAge()
print(f"Age after increment: {animal1.getAge()}")  # Output: Age after increment: 8
