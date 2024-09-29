## Inheritance in Python (Basic)

This example demonstrates how to implement **inheritance** in Python, where subclasses can inherit properties and methods from a parent class. In this case, the `Animal` class serves as the parent class, while `Dog`, `Cat`, and `Sheep` are its subclasses.

### Structure

- **File**: `basic.py`
  - Contains a parent class `Animal`
  - Contains child classes `Dog`, `Cat`, and `Sheep`
  - Demonstrates how to use basic accessors and mutators, as well as the `super()` function to access parent class methods.

### Key Concepts

1. **Inheritance**:
   - A way to create a new class that is based on an existing class, inheriting its properties and methods.

2. **Accessing Parent Class Methods**:
   - The `super()` function allows child classes to call methods from the parent class, facilitating code reuse.

---

### Class: `Animal`

```python
class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def setName(self, new_name: str):
        self.name = new_name

    def setAge(self, new_age: int):
        if new_age in range(0, 100):
            self.age = new_age

class Dog(Animal):
    def bark(self) -> str:
        return "Woof!"

class Cat(Animal):
    def meow(self) -> str:
        return "Meow!"

class Sheep(Animal):
    def baa(self) -> str:
        return "Baa!"
```

---

### Usage

- **Create objects of subclasses**:
  ```python
  dog = Dog("Rex", 3)
  cat = Cat("Whiskers", 2)
  sheep = Sheep("Dolly", 4)
  ```

- **Access values using accessor methods**:
  ```python
  print(dog.getName())  # Output: Rex
  print(cat.getAge())    # Output: 2
  ```

- **Modify values using mutator methods**:
  ```python
  sheep.setName("Dolly II")
  print(sheep.getName())  # Output: Dolly II
  ```

- **Use subclass-specific methods**:
  ```python
  print(dog.bark())  # Output: Woof!
  print(cat.meow())  # Output: Meow!
  print(sheep.baa())  # Output: Baa!
  ```

This basic example introduces students to the concept of inheritance, demonstrating how child classes can extend and specialize the behavior of a parent class.

---

## Inheritance in Python (Advanced with Property Decorators)

This example explores a more advanced approach to implementing **inheritance** in Python, where subclasses inherit properties and methods from a parent class while utilizing **property decorators** for accessors and mutators. The `Animal` class serves as the parent class, while `Dog`, `Cat`, and `Sheep` are its subclasses.

### Structure

- **File**: `advance.py`
  - Contains a parent class `Animal`
  - Contains child classes `Dog`, `Cat`, and `Sheep`
  - Demonstrates the use of `@property` decorators for defining getters and setters, as well as passing keyword arguments to `super()`.

### Key Concepts

1. **Inheritance**:
   - Enables the creation of a new class based on an existing class, allowing for the reuse of code and properties.

2. **Property Decorators**:
   - The `@property` decorator allows for encapsulation while making the code more readable and Pythonic.

3. **Using `super()` with `**kwargs`**:
   - Allows subclasses to pass arguments to the parent class constructor dynamically, facilitating flexible initialization.

---

### Class: `Animal`

```python
class Animal:
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self) -> str:
        return self.__gender

    @name.setter
    def name(self, new_name: str):
        if new_name:
            self.__name = new_name

class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str, breed: str):
        super().__init__(name, age, gender)
        self.breed = breed

    def bark(self) -> str:
        return "Woof!"

class Cat(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def meow(self) -> str:
        return "Meow!"

class Sheep(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def baa(self) -> str:
        return "Baa!"
```

---

### Usage

- **Create objects of subclasses**:
  ```python
  dog = Dog("Rex", 3, "Male", "German Shepherd")
  cat = Cat("Whiskers", 2, "Female")
  sheep = Sheep("Dolly", 4, "Female")
  ```

- **Access values using property methods**:
  ```python
  print(dog.name)  # Output: Rex
  print(cat.age)    # Output: 2
  ```

- **Modify values using property setter**:
  ```python
  sheep.name = "Dolly II"
  print(sheep.name)  # Output: Dolly II
  ```

- **Use subclass-specific methods**:
  ```python
  print(dog.bark())  # Output: Woof!
  print(cat.meow())  # Output: Meow!
  print(sheep.baa())  # Output: Baa!
  ```

### Summary

This advanced example illustrates how Python's inheritance model allows for the reuse and extension of functionality, while property decorators enhance encapsulation and readability. The use of `super()` with `**kwargs` provides a flexible mechanism for initializing parent classes.

---
Programming Club of Curtin Colombo