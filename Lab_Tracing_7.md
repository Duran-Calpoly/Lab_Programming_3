# Lab Tracing Exercise 7: Object Construction and State

**Follows:** Lecture 28 - Objects I: Compound Data  
**Format:** One class meeting; tracing and debugger observation only  
**File:** `trace7.py`

## Motivation

In Lecture 28, you learned that a class describes a kind of object and that an instance groups related values in named attributes. The current values of those attributes make up an object's **state**.

In this lab, you will trace how objects are constructed and initialized, how expressions access attributes, and how attribute assignments change object state. You will also observe that two separate constructor calls create two independent instances.

**You are not being asked to implement any functions or classes.** Copy each complete program as provided, predict its behavior, and inspect its execution in the debugger.

## Course Learning Objectives

- Use an IDE and a visual debugger to step through a Python program.
- Trace object construction, parameter bindings, and attribute assignments.
- Evaluate expressions involving object attributes.
- Explain object state and distinguish two independently constructed instances.

## Setup

1. Create a Python file named `trace7.py`.
2. For each task, replace the contents of the file with the provided program.
3. **Make your predictions before running the debugger.**
4. Set the indicated breakpoint and use **Step Into** or **Step Over** as directed.
5. Expand objects in the Variables frame to inspect their attributes. Record observations after executing the indicated lines.

There are **five tracing tasks**. Complete them in order.

---

## Task 1: Constructing and Initializing an Object

Copy this program into `trace7.py`:

```python
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


p = Point(3.0, 4.0)
print(p.x)
print(p.y)
```

### Predictions

1. How many `Point` instances will this program create?
2. What values will be bound to the parameters `x` and `y` in `__init__`?
3. What will `self` refer to while `__init__` is running?
4. What attributes will the new object have when initialization finishes?

### Trace

Set a breakpoint on `p = Point(3.0, 4.0)`. Start the debugger and **Step Into** the call. At the beginning of `__init__`, examine `self`, `x`, and `y`. Step through each attribute assignment.

| Checkpoint | Parameter / variable bindings | Attributes of the new object |
|---|---|---|
| Beginning of `__init__` | | |
| After `self.x = x` | | |
| After `self.y = y` | | |
| After the constructor call completes | | |

### Questions

1. Does the new instance already exist when `__init__` begins?
2. What does `self.x = x` do to that instance?
3. After initialization, what does the variable `p` refer to?
4. What is printed? Explain the role of `__init__` in one or two sentences.

---

## Task 2: Expressions Involving Attributes

Replace the program with:

```python
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


p = Point(3, 7)
total = p.x + p.y
difference = p.y - p.x
comparison = p.x < p.y

print(total)
print(difference)
print(comparison)
```

### Predictions

| Expression | Predicted value |
|---|---|
| `p.x` | |
| `p.y` | |
| `p.x + p.y` | |
| `p.y - p.x` | |
| `p.x < p.y` | |

### Trace

Set a breakpoint on `p = Point(3, 7)`. Use **Step Over** to execute each statement, expanding `p` to inspect its attributes.

| After executing | Variables and values observed | State of `p` |
|---|---|---|
| `p = Point(3, 7)` | | |
| `total = p.x + p.y` | | |
| `difference = p.y - p.x` | | |
| `comparison = p.x < p.y` | | |

### Questions

1. What do `total`, `difference`, and `comparison` contain?
2. Did reading `p.x` or `p.y` change the object's state?
3. How is accessing an attribute similar to reading a value from another compound data structure?

---

## Task 3: Changing Object State

Replace the program with:

```python
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


p = Point(2, 5)
p.x = 8
p.y = p.y + 3
result = p.x + p.y

print(result)
```

### Predictions

1. What are the initial values of `p.x` and `p.y`?
2. What will each attribute contain after the two assignments?
3. What value will be bound to `result`?
4. How many `Point` objects will exist at the end?

### Trace

Set a breakpoint on `p = Point(2, 5)` and **Step Over** the statements. Observe the same object's attributes after every assignment.

| After executing | `p.x` | `p.y` | `result` (if bound) |
|---|---|---|---|
| `p = Point(2, 5)` | | | |
| `p.x = 8` | | | |
| `p.y = p.y + 3` | | | |
| `result = p.x + p.y` | | | |

### Questions

1. Did an attribute assignment create a new `Point` object or update the existing object?
2. Which part of the object's state changed after `p.x = 8`?
3. In your own words, what does **object state** mean?

---

## Task 4: Independent Instances of the Same Class

Replace the program with:

```python
class Dog:
    def __init__(self, name: str, breed: str, age: int):
        self.name = name
        self.breed = breed
        self.age = age


a = Dog("Sofia", "Maremma", 1)
b = Dog("Buddy", "Labrador", 3)
a.age = 2

print(a.name, a.age)
print(b.name, b.age)
```

### Predictions

1. How many `Dog` instances are created?
2. What are the initial attributes of each instance?
3. Does `a.age = 2` change the state of `a`, `b`, or both?

### Trace

Set a breakpoint on the first constructor call. **Step Into** each call to `Dog.__init__` to observe which new instance `self` refers to. Then **Step Over** the remaining assignments.

| Checkpoint | State of object referred to by `a` | State of object referred to by `b` |
|---|---|---|
| After first construction | | |
| After second construction | | |
| After `a.age = 2` | | |

### Questions

1. Why do `a` and `b` refer to different objects?
2. Why does changing `a.age` not change `b.age`?
3. What does the class definition have in common across both instances, and what can differ?

---

## Task 5: The Same Data in a Dictionary and an Object

Replace the program with:

```python
class Student:
    def __init__(self, name: str, units: int):
        self.name = name
        self.units = units


record = {"name": "Ada", "units": 12}
student = Student("Ada", 12)

record["units"] = 16
student.units = 16

record_name = record["name"]
student_name = student.name

print(record_name, record["units"])
print(student_name, student.units)
```

### Predictions

1. What does `record["units"]` evaluate to immediately after dictionary creation?
2. What does `student.units` evaluate to immediately after construction?
3. What will the two print statements display?

### Trace

Set a breakpoint on `record = ...` and **Step Over** each statement. Expand the dictionary and the `Student` instance in the Variables frame.

| Checkpoint | Dictionary contents | Student attributes |
|---|---|---|
| After `student = Student(...)` | | |
| After both updates to `units` | | |
| After both name lookups | | |

### Questions

1. What is similar about the information stored by the dictionary and the object?
2. Why do you write `record["name"]` for a dictionary but `student.name` for this object?
3. How does the `Student` class describe the structure of its instances?

---

## Demonstration

Show an instructor:

- the debugger paused inside `__init__`, with `self` referring to the instance being initialized;
- attributes appearing as initialization proceeds;
- attribute expressions evaluated without changing object state;
- an attribute assignment changing an existing instance;
- two independently constructed instances with different states; and
- the difference between dictionary-key access and object-attribute access.

Be prepared to explain the terms **class**, **instance**, **constructor call**, **`__init__`**, **`self`**, **attribute**, and **object state**.

## Looking Ahead

In Lecture 29 you will explore **methods** that operate on object state, references shared by multiple variables, and collections containing objects. The next programming lab will ask you to implement and test these behaviors rather than only trace existing code.
