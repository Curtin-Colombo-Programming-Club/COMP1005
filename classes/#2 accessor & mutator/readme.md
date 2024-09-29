## Accessors and Mutators in Python (Basic)

This example demonstrates how to implement **accessor** (getter) and **mutator** (setter) methods using standard function definitions in Python classes. Accessors are used to retrieve private attribute values, while mutators allow controlled modification of these attributes.

### Structure

- **File**: `basic.py`
  - Contains a class `Animal`
  - Demonstrates how to use getter and setter methods to access and modify class attributes.

### Key Concepts

1. **Accessors**:
   - Methods used to access (or "get") the value of a private attribute.
   - In this file, `getName()`, `getAge()`, and `getGender()` are accessor methods.
   
2. **Mutators**:
   - Methods used to modify (or "set") the value of a private attribute.
   - In this file, `setName()`, `setAge()`, and `incrAge()` are mutator methods.
   
3. **Method Chaining**:
   - Mutator methods return `self`, allowing you to call multiple methods in a single line (method chaining).

---

### Class: `Animal`

```python
class Animal:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def getGender(self) -> str:
        return self.gender

    def setName(self, new_name: str) -> Self:
        self.name = new_name
        return self

    def setAge(self, new_age: int) -> Self:
        if new_age in range(0, 100):
            self.age = new_age
        return self

    def incrAge(self) -> Self:
        self.age += 1
        return self
```

---

### Usage

- **Create an object**:
  ```python
  animal1 = Animal("Lion", 5, "Male")
  ```

- **Access values using accessor methods**:
  ```python
  print(animal1.getName())  # Output: Lion
  print(animal1.getAge())   # Output: 5
  ```

- **Modify values using mutator methods**:
  ```python
  animal1.setName("Tiger").setAge(6)
  print(animal1.getName())  # Output: Tiger
  ```

- **Increment the age**:
  ```python
  animal1.incrAge()
  print(animal1.getAge())   # Output: 7
  ```

This basic example introduces students to the concept of encapsulation, allowing controlled access and modification of private attributes through getter and setter methods.

---

## Accessors and Mutators in Python (Advanced with Property Decorators)

This example explores a more advanced approach to implementing **accessor** (getter) and **mutator** (setter) methods using **property decorators** in Python. Property decorators allow accessors and mutators to act like regular attributes, making the code more Pythonic and readable.

### Structure

- **File**: `advance.py`
  - Contains a class `Animal`
  - Demonstrates the use of `@property` decorators for defining getters and setters.

### Key Concepts

1. **Encapsulation**:
   - Attributes like `__name`, `__age`, and `__gender` are **private** (prefixed with double underscores) to restrict direct access.

2. **Property Decorators**:
   - The `@property` decorator turns a method into a getter, allowing access to private attributes as if they were public attributes.
   - The `@property_name.setter` decorator is used to define a corresponding setter for the attribute.

3. **Data Validation in Setters**:
   - Setters can include validation to control what values can be assigned to an attribute. For instance, `name` is updated only if it's a non-empty string.

---

### Class: `Animal`

```python
class Animal:
    def __init__(self, _name: str, _age: int, _gender: str):
        self.__name = _name
        self.__age = _age
        self.__gender = _gender

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
    def name(self, _new_name: str) -> Self:
        if _new_name and isinstance(_new_name, str):
            self.__name = _new_name
        return self

    def aging(self) -> Self:
        self.__age += 1
        return self
```

---

### Usage

- **Create an object**:
  ```python
  animal1 = Animal("Elephant", 10, "Female")
  ```

- **Access values using property methods**:
  ```python
  print(animal1.name)    # Output: Elephant
  print(animal1.age)     # Output: 10
  print(animal1.gender)  # Output: Female
  ```

- **Modify values using property setter**:
  ```python
  animal1.name = "Giraffe"
  print(animal1.name)    # Output: Giraffe
  ```

- **Increment the age using `aging()` method**:
  ```python
  animal1.aging()
  print(animal1.age)     # Output: 11
  ```

- **Attempt to set an invalid name**:
  ```python
  animal1.name = ""
  print(animal1.name)    # Output: Giraffe  (remains unchanged)
  ```

### Summary

This advanced example illustrates how Python’s `@property` and `@setter` decorators simplify the process of defining getters and setters, while still preserving encapsulation. The example also shows how to include validation logic in setter methods to ensure data integrity.

---

Programming Club of Curtin Colombo