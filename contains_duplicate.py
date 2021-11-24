import unittest

# Given an integer array nums, return true if any value
# appears at least twice in the array,
# and return false if every element is distinct.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
from typing import List, Set


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual(True, contains_duplicate(self, [1, 2, 3, 1]))

    def test_something_2(self):
        self.assertEqual(False, contains_duplicate(self, [1, 2, 3, 4]))

    def test_something_3(self):
        self.assertEqual(True, contains_duplicate(self, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == '__main__':
    unittest.main()


def contains_duplicate(self, nums: List[int]) -> bool:
    unique_nums = set()
    for index in range(0, len(nums)):
        unique_nums.add(nums[index])
        if len(unique_nums) - 1 < index:
            return True
    return False
