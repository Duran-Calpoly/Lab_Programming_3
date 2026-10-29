# Lab Programming Exercise 3: Methods and Collections of Objects

**Follows:** Lecture 29 - Objects II: Methods, Aliasing, and Collections  
**Format:** One class meeting; implementation and unit testing  
**Repository:** https://github.com/devfirejedi4/CSC1001-Lab-Programming-Exercise-3

## Motivation

In the tracing lab, you observed how a class defines the attributes of its instances and how assignments change object state. In Lecture 29, you learned that **methods** define operations on that state, that variables can refer to the same object, and that collections can hold references to objects.

In this lab, you will **write and test code** that combines those ideas. You will implement:

- a **query method** that computes a value without changing the object;
- a **mutating method** that updates an object's attributes;
- two functions that process **lists of objects**; and
- methods on an object that **contains a list of other objects**.

The lab has **four programming tasks**. For every task, write multiple unit tests and run the full test suite. Debugging is a tool for fixing code, but tracing tables are not required.

## Course Learning Objectives

- Design, implement, and test functions and methods operating on compound data.
- Distinguish query methods from methods that change object state.
- Write tests that account for object references, identity, and aliasing.
- Process lists of objects without unintentionally copying or modifying them.
- Implement a class whose instances contain collections of other objects.

## Setup

1. Clone the repository in your IDE and open the project.
2. You will work with these files:

   ```text
   data.py
   data_tests.py
   lab.py
   lab_tests.py
   ```

3. Review the supplied `Point` class in `data.py`. It has `x` and `y` attributes. The instructor's starter version for this lab will also provide the method signatures and `PointPath` skeleton described below.
4. Run the provided tests before making changes.
5. Implement the methods for Tasks 1, 2, and 4 in `data.py` and test them in `data_tests.py`. Implement the functions for Task 3 in `lab.py` and test them in `lab_tests.py`.

The provided `Time` class, if present in the repository, is **not part of this lab**. Do not modify it.

## Starter Data Representation

A point in two-dimensional space has two attributes:

```python
p = data.Point(3.0, 4.0)
# p.x is 3.0 and p.y is 4.0
```

For the exercises below, `data.py` should have these **unfinished method signatures** (the instructor will provide this starter structure):

```python
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        raise NotImplementedError

    def translate(self, dx: float, dy: float) -> None:
        raise NotImplementedError


class PointPath:
    def __init__(self, name: str):
        self.name = name
        self.points: list[Point] = []

    def add_point(self, point: Point) -> None:
        raise NotImplementedError

    def total_length(self) -> float:
        raise NotImplementedError
```

Do not replace these methods with ordinary functions. Implement them **inside their classes**.

## Design Recipe

For each task:

1. State the purpose, inputs, outputs, and whether the operation **changes object state**.
2. Identify relevant attributes and existing functions or methods.
3. Work through examples and important boundary cases.
4. Write multiple unit tests, including tests for any promised non-mutation or reference behavior.
5. Complete the implementation and run all tests.
6. Investigate failures, correct the code, and run all tests again.

---

## Task 1: A Query Method - `Point.distance_to`

Implement the `distance_to` method in `Point`.

```python
def distance_to(self, other: "Point") -> float:
```

It must return the Euclidean distance from `self` to `other`, **without changing either point**. For points `(x1, y1)` and `(x2, y2)`, the distance is:

```text
sqrt((x2 - x1)**2 + (y2 - y1)**2)
```

You may import `sqrt` from `math`.

Example:

```python
first = data.Point(0, 0)
second = data.Point(3, 4)
result = first.distance_to(second)
# result is 5.0
```

### Testing

Write multiple tests in `data_tests.py`. Include points with negative coordinates, a point compared with itself, reversing argument order, and confirmation that neither point's attributes change.

### Questions to Consider

1. What does `self` refer to during `first.distance_to(second)`?
2. What does `other` refer to?
3. Why is this a **query method** rather than a mutating method?

---

## Task 2: A Mutating Method - `Point.translate`

Implement `translate` in `Point`.

```python
def translate(self, dx: float, dy: float) -> None:
```

It must **change the existing point** by increasing `self.x` by `dx` and `self.y` by `dy`. It must not construct a replacement point. It returns `None`.

Example:

```python
p = data.Point(2, 5)
p.translate(3, -2)
# p.x is 5 and p.y is 3
```

### Testing

Write multiple tests in `data_tests.py` that check positive, negative, and zero offsets. Include **both** of the following reference situations:

```python
p = data.Point(2, 5)
alias = p
alias.translate(3, -2)
# Both names still refer to the same, now-modified point.
```

```python
first = data.Point(2, 5)
second = data.Point(2, 5)
first.translate(3, -2)
# The separate second point should not change.
```

Use `self.assertIs(...)` to check shared identity, and check attribute values to confirm which object changed.

### Questions to Consider

1. Why does translating `alias` also change the state observed through `p`?
2. Why does translating `first` not change `second`?
3. What is the difference between a query method and a mutating method?

---

## Task 3: Lists of Objects - Map and Filter

Implement **two functions** in `lab.py`. Unlike Tasks 1 and 2, these are ordinary functions, not methods.

### Part A: `x_coordinates`

```python
def x_coordinates(points: list[data.Point]) -> list[float]:
```

Return a new list containing the `x` attribute of each point, in the original order.

Example:

```python
points = [
    data.Point(1.0, 2.0),
    data.Point(3.0, 4.0),
    data.Point(-2.0, 5.0),
]
# x_coordinates(points) returns [1.0, 3.0, -2.0]
```

Do not modify the input list or any input point. This is a **map** pattern.

### Part B: `are_in_positive_quadrant`

```python
def are_in_positive_quadrant(points: list[data.Point]) -> list[data.Point]:
```

Return a new list of the existing points whose `x` and `y` attributes are **both greater than zero**. Preserve their order. Points lying on an axis do not qualify.

Example:

```python
first = data.Point(1, 2)
second = data.Point(-3, 4)
third = data.Point(5, 6)
points = [first, second, third]

result = lab.are_in_positive_quadrant(points)
# result contains references to first and third, in that order.
```

**Do not construct new `Point` objects to fill the result list.** This is a **filter** pattern.

### Testing

Write multiple tests for **each function** in `lab_tests.py`. Include empty lists, one-element lists, negative values, and zero coordinates. For the filter, confirm that the returned entries are the **same objects** as those in the input using `self.assertIs(...)`. Also confirm that the input list and its points remain unchanged.

### Questions to Consider

1. Why does the map produce numbers while the filter produces `Point` references?
2. How does a new result list differ from creating new point objects?
3. Why does a point on an axis fail the first-quadrant test?

---

## Task 4: An Object Containing a List - `PointPath`

A path has a name and an ordered list of `Point` objects. The `PointPath` constructor in `data.py` already initializes:

```python
self.name = name
self.points = []
```

Implement **both** of the following methods on `PointPath`.

### Part A: `add_point`

```python
def add_point(self, point: Point) -> None:
```

Append the **existing `Point` object** to `self.points`. Do not create a copy. Do not return a value.

Example:

```python
path = data.PointPath("Walk")
p = data.Point(0, 0)
path.add_point(p)
# path.points[0] is the same object as p
```

### Part B: `total_length`

```python
def total_length(self) -> float:
```

Return the sum of Euclidean distances between **consecutive points** in the path. Reuse the `Point.distance_to` method you wrote in Task 1. Do not duplicate the distance formula.

For a path containing fewer than two points, return `0.0`. The method must not change the path or any point.

Example:

```python
path = data.PointPath("Walk")
path.add_point(data.Point(0, 0))
path.add_point(data.Point(3, 4))
path.add_point(data.Point(6, 4))

result = path.total_length()
# result is 8.0: 5.0 + 3.0
```

### Testing

Write multiple tests in `data_tests.py` for empty paths, one-point paths, and paths containing at least two segments. Verify:

- points remain in the order they were added;
- `add_point` stores the original object reference, using `self.assertIs(...)`;
- `total_length` calls on a path produce the expected result;
- calling `total_length` does not change the path or its points.

### Questions to Consider

1. What does `self` refer to during `path.add_point(p)`?
2. What does `self.points` contain?
3. How can you access the x-coordinate of the first point with `path.points[0].x`?
4. Why is `distance_to` preferable to reimplementing the calculation?

---

## Testing Requirements

For every task:

- Write multiple unit tests, not only one example test.
- Include representative and boundary cases.
- Test empty collections where applicable.
- Verify mutation **only** where the requirements permit it.
- Verify reference identity where the requirements specify keeping an existing object.
- Run the full test suite before demonstrating the lab.

## Review

| Function or method | Kind | Main concept |
|---|---|---|
| `Point.distance_to` | Query method | `self`, other object, no mutation |
| `Point.translate` | Mutating method | Object state and aliasing |
| `x_coordinates` | Function | Map over a list of objects |
| `are_in_positive_quadrant` | Function | Filter; preserve object references |
| `PointPath.add_point` | Mutating method | Object containing a list of objects |
| `PointPath.total_length` | Query method | Iterate over objects; reuse a method |

## Demonstration

Show an instructor:

- the completed implementations in `data.py` and `lab.py`;
- passing unit tests in `data_tests.py` and `lab_tests.py`;
- a query method that does not modify either point;
- a mutating method with an aliasing test;
- a list-processing function that preserves the original point references; and
- a `PointPath` storing points and computing the length of a multi-segment path.

Be prepared to explain **methods**, **`self`**, **query versus mutation**, **aliasing**, **identity**, **lists of objects**, **objects containing lists**, and **method reuse**.

## Looking Ahead

These exercises combined functions, methods, and compound data. The next programming exercise will apply your existing iteration and data-representation skills to **searching and sorting**.
