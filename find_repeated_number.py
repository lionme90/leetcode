import unittest
from typing import List


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual(None, find_first_recurrent([2, 3, 5, 6]))

    def test_something_2(self):
        self.assertEqual(2, find_first_recurrent([2, 2, 5, 6]))

    def test_something_3(self):
        self.assertEqual(3, find_first_recurrent([2, 3, 5, 3]))


if __name__ == '__main__':
    unittest.main()


def find_first_recurrent(nums: List[int]):
    unique_nums = set()
    for n in nums:
        if n in unique_nums:
            return n
        else:
            unique_nums.add(n)
    return None
