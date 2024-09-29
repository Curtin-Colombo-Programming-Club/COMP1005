from typing import Self

# Parent class 'Animal'
class Animal:
    def __init__(self, **kwargs):
        """
        The initializer (constructor) for Animal.
        Takes in common parameters for all animals using **kwargs: name, age, and gender.
        """
        self._name = kwargs.get("name", "Unknown")  # Default name if not provided
        self._age = kwargs.get("age", 0)            # Default age is 0
        self._gender = kwargs.get("gender", "Unknown")  # Default gender is Unknown

    # Accessor and Mutator for 'name' using property decorator
    @property
    def name(self) -> str:
        """Getter for name."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> Self:
        """Setter for name."""
        if new_name and isinstance(new_name, str):
            self._name = new_name
        return self

    # Accessor and Mutator for 'age' using property decorator
    @property
    def age(self) -> int:
        """Getter for age."""
        return self._age

    @age.setter
    def age(self, new_age: int) -> Self:
        """Setter for age."""
        if 0 <= new_age <= 100:
            self._age = new_age
        return self

    # Accessor and Mutator for 'gender' using property decorator
    @property
    def gender(self) -> str:
        """Getter for gender."""
        return self._gender

    @gender.setter
    def gender(self, new_gender: str) -> Self:
        """Setter for gender."""
        if new_gender and isinstance(new_gender, str):
            self._gender = new_gender
        return self


# Child class 'Dog' inheriting from 'Animal'
class Dog(Animal):
    def __init__(self, **kwargs):
        """
        The initializer for Dog.
        Uses 'super()' to call the initializer of the parent class 'Animal'.
        Adds a new attribute 'breed' specific to dogs.
        """
        super().__init__(**kwargs)  # Initialize parent class with kwargs
        self._breed = kwargs.get("breed", "Unknown")  # Default breed if not provided

    # Accessor and Mutator for 'breed' using property decorator
    @property
    def breed(self) -> str:
        """Getter for breed."""
        return self._breed

    @breed.setter
    def breed(self, new_breed: str) -> Self:
        """Setter for breed."""
        if new_breed and isinstance(new_breed, str):
            self._breed = new_breed
        return self


# Child class 'Cat' inheriting from 'Animal'
class Cat(Animal):
    def __init__(self, **kwargs):
        """
        The initializer for Cat.
        Uses 'super()' to call the initializer of the parent class 'Animal'.
        Adds a new attribute 'color' specific to cats.
        """
        super().__init__(**kwargs)  # Initialize parent class with kwargs
        self._color = kwargs.get("color", "Unknown")  # Default color if not provided

    # Accessor and Mutator for 'color' using property decorator
    @property
    def color(self) -> str:
        """Getter for color."""
        return self._color

    @color.setter
    def color(self, new_color: str) -> Self:
        """Setter for color."""
        if new_color and isinstance(new_color, str):
            self._color = new_color
        return self


# Child class 'Sheep' inheriting from 'Animal'
class Sheep(Animal):
    def __init__(self, **kwargs):
        """
        The initializer for Sheep.
        Uses 'super()' to call the initializer of the parent class 'Animal'.
        Adds a new attribute 'wool_type' specific to sheep.
        """
        super().__init__(**kwargs)  # Initialize parent class with kwargs
        self._wool_type = kwargs.get("wool_type", "Unknown")  # Default wool type if not provided

    # Accessor and Mutator for 'wool_type' using property decorator
    @property
    def wool_type(self) -> str:
        """Getter for wool type."""
        return self._wool_type

    @wool_type.setter
    def wool_type(self, new_wool_type: str) -> Self:
        """Setter for wool type."""
        if new_wool_type and isinstance(new_wool_type, str):
            self._wool_type = new_wool_type
        return self


# Example usage
if __name__ == "__main__":
    # Create instances of Dog, Cat, and Sheep using keyword arguments
    dog = Dog(name="Buddy", age=5, gender="Male", breed="Golden Retriever")
    cat = Cat(name="Whiskers", age=3, gender="Female", color="Black")
    sheep = Sheep(name="Dolly", age=4, gender="Female", wool_type="Merino")

    # Accessing attributes using property decorators
    print(f"Dog's name: {dog.name}, Breed: {dog.breed}")
    print(f"Cat's name: {cat.name}, Color: {cat.color}")
    print(f"Sheep's name: {sheep.name}, Wool type: {sheep.wool_type}")

    # Modifying attributes using property decorators
    dog.name = "Max"
    dog.breed = "Labrador"
    print(f"Updated Dog's name: {dog.name}, Updated Breed: {dog.breed}")
