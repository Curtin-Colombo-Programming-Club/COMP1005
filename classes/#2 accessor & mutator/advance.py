from typing import Self

# Define a class 'Animal' with encapsulated attributes and accessor/mutator methods
class Animal:
    # The initializer (constructor) to set up initial attributes
    def __init__(self, _name: str, _age: int, _gender: str):
        # Encapsulated attributes (private) with double underscores
        self.__name: str = _name  # Private string attribute for the animal's name
        self.__age: int = _age    # Private integer attribute for the animal's age
        self.__gender: str = _gender  # Private string attribute for the animal's gender

    # Accessor methods (using the property decorator)

    @property
    def name(self) -> str:
        """
        Accessor method (getter) for the 'name' attribute.
        The @property decorator allows access like an attribute, not a method.
        """
        return self.__name

    @property
    def age(self) -> int:
        """
        Accessor method (getter) for the 'age' attribute.
        """
        return self.__age
    
    @property
    def gender(self) -> str:
        """
        Accessor method (getter) for the 'gender' attribute.
        """
        return self.__gender

    # Mutator methods (setters)

    @name.setter
    def name(self, _new_name: str) -> Self:
        """
        Mutator method (setter) for the 'name' attribute.
        The @name.setter decorator allows updating the name like an attribute.
        Ensures the new name is a non-empty string before updating.
        """
        # Condition: If the new name is valid (non-empty and of type str), update it
        if _new_name and isinstance(_new_name, str):
            self.__name = _new_name
        return self

    def aging(self) -> Self:
        """
        Mutator method to increment the 'age' attribute by 1.
        This doesn't need a setter decorator because it modifies the attribute directly.
        """
        self.__age += 1  # Increment the age by 1
        return self


# Example usage:

# Creating an instance of the Animal class
animal1 = Animal("Elephant", 10, "Female")

# Accessing attributes using property methods (getters)
print(f"Name: {animal1.name}")  # Output: Name: Elephant
print(f"Age: {animal1.age}")    # Output: Age: 10
print(f"Gender: {animal1.gender}")  # Output: Gender: Female

# Modifying the name attribute using the property setter
animal1.name = "Giraffe"
print(f"Updated Name: {animal1.name}")  # Output: Updated Name: Giraffe

# Incrementing age using the aging method
animal1.aging()
print(f"Age after aging: {animal1.age}")  # Output: Age after aging: 11

# Trying to set an invalid name (empty string)
animal1.name = ""
print(f"Name after invalid update: {animal1.name}")  # Output: Name after invalid update: Giraffe
