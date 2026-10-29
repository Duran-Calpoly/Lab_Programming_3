"""Lab Programming Exercise 3: Methods and Collections of Objects.

Complete the TODOs below. Do not change the function/method names,
parameters, or return types.

Tasks 1, 2, and 4: Complete the methods in Point and PointPath.
Task 3: Complete the two standalone functions below.
"""


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Task 1: Query method
    def distance_to(self, other: "Point") -> float:
        """Return the Euclidean distance to other without changing either point."""
        # TODO: Implement this method.
        raise NotImplementedError

    # Task 2: Mutating method
    def translate(self, dx: float, dy: float) -> None:
        """Move this same point by dx and dy. Return None."""
        # TODO: Implement this method.
        raise NotImplementedError


# Task 3A: Map over a list of objects
def x_coordinates(points: list[Point]) -> list[float]:
    """Return the x-coordinates of points, in their original order."""
    # TODO: Implement this function.
    raise NotImplementedError


# Task 3B: Filter a list of objects
def are_in_positive_quadrant(points: list[Point]) -> list[Point]:
    """Return existing points where x > 0 and y > 0, in their original order."""
    # TODO: Implement this function. Do not copy or recreate Point objects.
    raise NotImplementedError


class PointPath:
    def __init__(self, name: str):
        self.name = name
        self.points: list[Point] = []

    # Task 4A: Store a reference to an existing point
    def add_point(self, point: Point) -> None:
        """Add this point to the path without creating a copy. Return None."""
        # TODO: Implement this method.
        raise NotImplementedError

    # Task 4B: Query method and method reuse
    def total_length(self) -> float:
        """Sum distances between consecutive points without changing the path."""
        # TODO: Implement this method using Point.distance_to.
        # A path with fewer than two points has length 0.0.
        raise NotImplementedError
