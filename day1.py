"""Lab Tracing Exercise 7, Day 1: Object Construction and State.

All five tasks are complete programs adapted into functions so they can
be traced in the debugger and checked with unittest.

Set a breakpoint inside a task, then run this file or test_1.py.
"""


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Dog:
    def __init__(self, name: str, breed: str, age: int):
        self.name = name
        self.breed = breed
        self.age = age


class Student:
    def __init__(self, name: str, units: int):
        self.name = name
        self.units = units


def task_1():
    """Construct and initialize a Point; return it for inspection."""
    p = Point(3.0, 4.0)
    return p


def task_2():
    """Evaluate expressions that read a Point's attributes."""
    p = Point(3, 7)
    total = p.x + p.y
    difference = p.y - p.x
    comparison = p.x < p.y
    return p, total, difference, comparison


def task_3():
    """Change the state of an existing Point."""
    p = Point(2, 5)
    p.x = 8
    p.y = p.y + 3
    result = p.x + p.y
    return p, result


def task_4():
    """Construct two independent Dog instances and change only one."""
    a = Dog("Sofia", "Maremma", 1)
    b = Dog("Buddy", "Labrador", 3)
    a.age = 2
    return a, b


def task_5():
    """Compare dictionary key access with object attribute access."""
    record = {"name": "Ada", "units": 12}
    student = Student("Ada", 12)

    record["units"] = 16
    student.units = 16

    record_name = record["name"]
    student_name = student.name
    return record, student, record_name, student_name


if __name__ == "__main__":
    p = task_1()
    print(p.x)
    print(p.y)

    p, total, difference, comparison = task_2()
    print(total)
    print(difference)
    print(comparison)

    p, result = task_3()
    print(result)

    a, b = task_4()
    print(a.name, a.age)
    print(b.name, b.age)

    record, student, record_name, student_name = task_5()
    print(record_name, record["units"])
    print(student_name, student.units)
