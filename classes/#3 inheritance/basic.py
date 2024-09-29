from typing import Self

# Parent class 'Animal'
class Animal:
    def __init__(self, name: str, age: int, gender: str):
        """
        The initializer (constructor) for Animal.
        Takes in the common parameters for all animals: name, age, and gender.
        """
        self._name = name  # Protected attribute for the animal's name
        self._age = age    # Protected attribute for the animal's age
        self._gender = gender  # Protected attribute for the animal's gender

    # Accessor methods (getters)
    def getName(self) -> str:
        """Returns the name of the animal."""
        return self._name

    def getAge(self) -> int:
        """Returns the age of the animal."""
        return self._age

    def getGender(self) -> str:
        """Returns the gender of the animal."""
        return self._gender

    # Mutator methods (setters)
    def setName(self, new_name: str) -> Self:
        """Sets a new name for the animal."""
        if new_name and isinstance(new_name, str):
            self._name = new_name
        return self

    def setAge(self, new_age: int) -> Self:
        """Sets a new age for the animal."""
        if 0 <= new_age <= 100:
            self._age = new_age
        return self


# Child class 'Dog' inheriting from 'Animal'
class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str, breed: str):
        """
        The initializer for Dog.
        Uses 'super()' to call the initializer of the parent class 'Animal'.
        Adds a new attribute 'breed' specific to dogs.
        """
        super().__init__(name, age, gender)  # Initialize parent class
        self._breed = breed  # Attribute specific to Dog

    def getBreed(self) -> str:
        """Returns the breed of the dog."""
        return self._breed

    def setBreed(self, new_breed: str) -> Self:
        """Sets a new breed for the dog."""
        if new_breed and isinstance(new_breed, str):
            self._breed = new_breed
        return self


# Child class 'Cat' inheriting from 'Animal'
class Cat(Animal):
    def __init__(self, name: str, age: int, gender: str, color: str):
        """
        The initializer for Cat.
        Uses 'super()' to call the initializer of the parent class 'Animal'.
        Adds a new attribute 'color' specific to cats.
        """
        super().__init__(name, age, gender)  # Initialize parent class
        self._color = color  # Attribute specific to Cat

    def getColor(self) -> str:
        """Returns the color of the cat."""
        return self._color

    def setColor(self, new_color: str) -> Self:
        """Sets a new color for the cat."""
        if new_color and isinstance(new_color, str):
            self._color = new_color
        return self


# Child class 'Sheep' inheriting from 'Animal'
class Sheep(Animal):
    def __init__(self, name: str, age: int, gender: str, wool_type: str):
        """
        The initializer for Sheep.
        Uses 'super()' to call the initializer of the parent class 'Animal'.
        Adds a new attribute 'wool_type' specific to sheep.
        """
        super().__init__(name, age, gender)  # Initialize parent class
        self._wool_type = wool_type  # Attribute specific to Sheep

    def getWoolType(self) -> str:
        """Returns the wool type of the sheep."""
        return self._wool_type

    def setWoolType(self, new_wool_type: str) -> Self:
        """Sets a new wool type for the sheep."""
        if new_wool_type and isinstance(new_wool_type, str):
            self._wool_type = new_wool_type
        return self


# Example usage:
if __name__ == "__main__":
    # Create instances of Dog, Cat, and Sheep
    dog = Dog("Buddy", 5, "Male", "Golden Retriever")
    cat = Cat("Whiskers", 3, "Female", "Black")
    sheep = Sheep("Dolly", 4, "Female", "Merino")

    # Accessing attributes using accessor methods
    print(f"Dog's name: {dog.getName()}, Breed: {dog.getBreed()}")
    print(f"Cat's name: {cat.getName()}, Color: {cat.getColor()}")
    print(f"Sheep's name: {sheep.getName()}, Wool type: {sheep.getWoolType()}")

    # Modifying attributes using mutator methods
    dog.setName("Max").setBreed("Labrador")
    print(f"Updated Dog's name: {dog.getName()}, Updated Breed: {dog.getBreed()}")
