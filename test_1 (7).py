"""Unit tests for Lab Tracing Exercise 7: Object Construction and State."""

import unittest

import day1


class TestTracingDay1(unittest.TestCase):
    def test_task_1_constructing_an_object(self):
        p = day1.task_1()
        self.assertEqual(3.0, p.x)
        self.assertEqual(4.0, p.y)

    def test_task_2_attribute_expressions(self):
        p, total, difference, comparison = day1.task_2()
        self.assertEqual(3, p.x)
        self.assertEqual(7, p.y)
        self.assertEqual(10, total)
        self.assertEqual(4, difference)
        self.assertEqual(True, comparison)

    def test_task_3_changing_state(self):
        p, result = day1.task_3()
        self.assertEqual(8, p.x)
        self.assertEqual(8, p.y)
        self.assertEqual(16, result)

    def test_task_4_independent_instances(self):
        a, b = day1.task_4()
        self.assertEqual("Sofia", a.name)
        self.assertEqual("Maremma", a.breed)
        self.assertEqual(2, a.age)
        self.assertEqual("Buddy", b.name)
        self.assertEqual("Labrador", b.breed)
        self.assertEqual(3, b.age)

    def test_task_5_dictionary_and_object(self):
        record, student, record_name, student_name = day1.task_5()
        self.assertEqual({"name": "Ada", "units": 16}, record)
        self.assertEqual("Ada", student.name)
        self.assertEqual(16, student.units)
        self.assertEqual("Ada", record_name)
        self.assertEqual("Ada", student_name)


if __name__ == "__main__":
    unittest.main()
