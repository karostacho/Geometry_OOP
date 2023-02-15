# The story

Do you love geometry? Our young friend Zigy (Zygfryd) loves it too. Unfortunately it's one-sided love. He's studying hard for his high-school exam, but with minor success. You've got to help him!
But how?
You'll write an Object Oriented Python Application to teach him geometry.

## Things you should know before you begin

1. Learn what are 4 pillars of OOP
2. What is inheritance
3. What is abstract class
4. What is static method vs what is instance method
5. What is UML diagram - how to represent classes and how they are connected to eachother?

# Requirements

In order to help Zigy you have to:

- [ ] Implement all `Shape` classes
- [ ] Implement `Program` class
- [ ] You are allowed to implement your own classes
- [ ] Remember about clean code
- [ ] Add UML.png file containing UML class diagram of classes
- [ ] Focus most on the OOP not the UI

PS: All the class names and functions should follow Python naming rules. Those here come mostly from C# but it would be too much work to change all of it.

# Specifications

Here you can find information what you have to implement.

## Program

This is the main entrance of the program.
The program allows user to create and add shapes to a list and do some things with it.

Running `Program` should show this menu:

```
Learn Geometry.
  What do you want to do?
  (1) Add new shape
  (2) Show all shapes
  (3) Show shape with the largest perimeter
  (4) Show shape with the largest area
  (5) Show formulas
  (0) Exit program
```

### Features

The program has to have 5 features.

#### 1. Add new shape

This feature allows user to add new shape to shapes list. User should be able to choose what kind of shapes he/she wants to add. Then he/she should specify attributes that a given shape requires.

#### 2. Show all shapes

This feature should print table containing all shapes added to the list.

#### 3. Show shape with the largest perimeter

This feature prints shape with the largest perimeter from a list of shapes.

#### 4. Show shape with the largest area

This feature prints shape with the largest area from a list of shapes.

#### 5. Show formulas

This feature should allow user to choose shape type and print it's formulas (perimeter, area).

## Classes

This is the most important part of this assignment. You've got to implement all of them.

### Shape Class

This is a so called _abstract class_. It means that we don't create instances of it. We only use it as a parent class for other concrete classes. This parent is a boilerplate for it's children. It contains attributes and methods that should be implemented in child classes.

#### Instance methods

##### `float CalculateArea()`

Returns the area of the shape as float.

##### `float CalculatePerimeter()`

Returns the perimeter of the shape as float.

##### `__str__()`?????

Returns information about given shape as string.

##### `String GetAreaFormula()`

Returns formula for the area of the shape as a string.

##### `String GetPerimeterFormula()`

Returns formula for the perimeter of the shape as string.

#### Static methods

##### `bool CheckIfArgsGreaterThanZero(float[] args)`

That method should be used in constructor of each specific shape. Returns true if any of args are greater than 0. Should raise `___Exception` (choose a proper Python exception) if any of the parameters is 0 or less (e.g. circle with negative radius doesn't exist).

...........................

### Circle Class

This class represents circle shape.

#### Parent class:

Shape

#### Attributes:

- name: `r`
  - data_type: float
  - description: circle radius length

#### Methods:

Implement all methods inherited from the parent class.

Required formulas:
Perimeter = 2×π×r
Area = π×r<sup>2</sup>

### Triangle Class

This class represents triangle shape.

#### Parent class:

Shape

#### Attributes:

- name: `a`
  - data_type: float
  - description: one side's length of a triangle
- name: `b`
  - data_type: float
  - description: second side's length of a triangle
- name: `c`
  - data_type: float
  - description: third side's length of a triangle

#### Methods:

Implement all methods inherited from the parent class.

Required formulas:
Perimeter = a + b + c
Area = sqrt(s(s-a)(s-b)(s-c)) use [Heron's Formula](https://en.wikipedia.org/wiki/Heron's_formula)

### Equilateral triangle Class

This is a triangle that has all sides equal.

#### Parent class:

Triangle

#### Attributes:

Hint: check if you can reuse attributes from the parent class or maybe triangle class? Tricky inheritance!

- name: `a`
  - data_type: float
  - description: side's length of a triangle

#### Methods:

Decide on your own if you have to implement/override inherited methods.

### Rectangle Class

This class represents rectangle shape.

#### Parent class:

Shape

#### Attributes:

- name: `a`
  - data_type: float
  - description: one side length
- name: `b`
  - data_type: float
  - description: second side length

#### Methods:

Implement all methods inherited from the parent class.

Required formulas:
Perimeter = 2a + 2b
Area = a×b

### Square Class

This is a rectangle that has all sides equal.

#### Parent class:

Rectangle

#### Attributes:

Hint: check if you can reuse attributes from the parent class. Inheritance once more!

- name: `a`
  - data_type: float
  - description: side's length of the square

#### Methods:

Decide on your own if you have to implement/override inherited methods.

### Regular pentagon Class

This is a shape with 5 sides. All sides are of the same length.

#### Parent class:

Shape

#### Attributes:

- name: `a`
  - data_type: float
  - description: side's length of the pentagon

#### Methods:

Implement all methods inherited from the parent class.

Required formulas:
Perimeter = 5a
Area = (a<sup>2</sup> sqrt(5(5+2sqrt(5))))/4

### ShapeList Class

This class is meant to hold geometrical shapes (objects that inherit from Shape class).

#### Attributes:

- name: `shapes`
  - data_type: list
  - description: list of Shape objects

#### Methods:

##### `CreateShapeList()`

Constructs ShapeList object

##### `AddShape(shape)`

Adds shape to shapes list

##### `Shape GetShapeAt(int index)`

Gets shape stored in `shapes` list under specified index

##### `GetLargestShapeByPerimeter()`

Returns shape with largest perimeter

##### `GetLargestShapeByArea()`

Returns shape with largest area

### Display

You have the freedom to choose how to display everything to the user.
