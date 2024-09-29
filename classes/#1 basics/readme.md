
## Basics of Python Classes

This section covers the basics of class declarations in Python. The code examples demonstrate how to create and work with classes using initializers (constructors), methods, and string representations. We will walk through the example provided in `basic.py`.

### Structure

- **File**: `basic.py`
  - Contains two classes: `MyClass` and `ParamClass`
  - Demonstrates class attributes, methods, and object behavior

### Key Concepts Covered

1. **Class Declaration**: 
   - Classes are a blueprint for creating objects.
   - Python's `class` keyword is used to define a class.
   
2. **Attributes and Methods**:
   - Classes can have attributes (variables) and methods (functions).
   - Attributes hold the state of an object, while methods define its behavior.

3. **`__init__` Method (Constructor)**:
   - The `__init__` method initializes an object when it is created.
   - This method can take arguments to set initial values for the object's attributes.

4. **`__str__` Method**:
   - The `__str__` method defines a string representation for the object, which is useful for debugging and printing.
   
5. **Method Behavior**:
   - Methods define the behavior of a class.
   - For example, `someFunction()` compares a given value to an attribute using the `is` operator.

---

### Class 1: `MyClass`

```python
class MyClass:
    def __init__(self) -> Self:
        self.attr1 = 1
        self.attr2 = "abc"

    def someFunction(self, val) -> bool:
        return self.attr2 is val

    def __str__(self) -> str:
        return f"MyClass(attr1: {self.attr1}, attr2: {self.attr2})\n"
```

#### Behavior:

- **Initialization**: 
  - When an instance of `MyClass` is created, `attr1` is set to `1` and `attr2` is set to `"abc"`.
  - Example:
    ```python
    my_instance = MyClass()
    ```

- **Comparing with `is`**:
  - The `someFunction()` method compares the `attr2` attribute with a passed value using the `is` operator (which checks for object identity, not just equality).
  - Example:
    ```python
    print(my_instance.someFunction("abc"))  # True
    ```

- **String Representation**:
  - The `__str__` method returns a readable string when the object is printed.
  - Example:
    ```python
    print(my_instance)  # Output: MyClass(attr1: 1, attr2: abc)
    ```

---

### Class 2: `ParamClass`

```python
class ParamClass:
    def __init__(self, param1: int, param2: str) -> Self:
        self.attr1 = param1
        self.attr2 = param2

    def someFunction(self, val) -> bool:
        return self.attr2 is val

    def __str__(self) -> str:
        return f"ParamClass(attr1: {self.attr1}, attr2: {self.attr2})\n"
```

#### Behavior:

- **Initialization with Parameters**:
  - `ParamClass` takes two arguments (`param1` and `param2`) during initialization, and assigns them to `attr1` and `attr2` respectively.
  - Example:
    ```python
    param_instance = ParamClass(10, "xyz")
    ```

- **Comparing with `is`**:
  - Similar to `MyClass`, this class uses the `someFunction()` method to compare `attr2` with the passed value using the `is` operator.
  - Example:
    ```python
    print(param_instance.someFunction("xyz"))  # True
    ```

- **String Representation**:
  - The `__str__` method provides a readable string format for printing the object.
  - Example:
    ```python
    print(param_instance)  # Output: ParamClass(attr1: 10, attr2: xyz)
    ```

---

### Running the Code

You can run the `basic.py` file to create instances of the classes and explore how they work. For example:

```python
# Create an instance of MyClass
my_instance = MyClass()

# Print the instance (calls __str__)
print(my_instance)

# Compare values with someFunction
print(my_instance.someFunction("abc"))

# Create an instance of ParamClass with parameters
param_instance = ParamClass(10, "xyz")

# Print the instance (calls __str__)
print(param_instance)

# Compare values with someFunction
print(param_instance.someFunction("xyz"))
```

### Summary

This example introduces:
- Basic class structure and initialization.
- Method behavior, object comparison, and string representation.
- Passing parameters during object creation.

In the next sections, we will explore more advanced concepts like inheritance, encapsulation, and polymorphism. Stay tuned!

---

Programming Club of Curtin Colombo