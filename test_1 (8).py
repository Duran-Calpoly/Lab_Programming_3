"""Starter unit tests for Lab Programming Exercise 3.

Run with: python -m unittest test_1.py

The tests for unfinished tasks will raise NotImplementedError until you
complete day1.py. Add more tests for the boundary and reference cases
listed in the lab handout.
"""

import unittest

import day1


class TestProgrammingDay1(unittest.TestCase):
    def test_point_constructor(self):
        point = day1.Point(3, 4)
        self.assertEqual(3, point.x)
        self.assertEqual(4, point.y)

    # Task 1
    def test_distance_to(self):
        first = day1.Point(0, 0)
        second = day1.Point(3, 4)

        self.assertEqual(5.0, first.distance_to(second))
        # TODO: Test negative coordinates, a point against itself,
        # reversing the order, and no mutation.

    # Task 2
    def test_translate(self):
        point = day1.Point(2, 5)
        result = point.translate(3, -2)

        self.assertEqual(5, point.x)
        self.assertEqual(3, point.y)
        self.assertEqual(None, result)
        # TODO: Test zero and negative offsets, aliasing, and
        # two independent points.

    # Task 3A
    def test_x_coordinates(self):
        points = [day1.Point(1, 2), day1.Point(3, 4), day1.Point(-2, 5)]

        self.assertEqual([1, 3, -2], day1.x_coordinates(points))
        # TODO: Test an empty list, one point, and no mutation.

    # Task 3B
    def test_are_in_positive_quadrant(self):
        first = day1.Point(1, 2)
        second = day1.Point(-3, 4)
        third = day1.Point(5, 6)

        result = day1.are_in_positive_quadrant([first, second, third])

        self.assertEqual(2, len(result))
        self.assertEqual(True, result[0] is first)
        self.assertEqual(True, result[1] is third)
        # TODO: Test axes, an empty list, and no mutation.

    # Task 4A
    def test_add_point(self):
        path = day1.PointPath("Walk")
        point = day1.Point(0, 0)
        result = path.add_point(point)

        self.assertEqual(1, len(path.points))
        self.assertEqual(True, path.points[0] is point)
        self.assertEqual(None, result)
        # TODO: Test several points and preservation of order.

    # Task 4B
    def test_total_length(self):
        path = day1.PointPath("Walk")
        # Set up the path directly so this test concentrates on total_length.
        path.points = [day1.Point(0, 0), day1.Point(3, 4), day1.Point(6, 4)]

        self.assertEqual(8.0, path.total_length())
        # TODO: Test empty and one-point paths and no mutation.


if __name__ == "__main__":
    unittest.main()
