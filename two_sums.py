import unittest

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
from typing import List, Dict


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual(two_sum(self, nums=[2, 7, 11, 15], target=9), [0, 1])

    def test_something_2(self):
        self.assertEqual(two_sum(self, nums=[3, 2, 4], target=6), [1, 2])

    def test_something_3(self):
        self.assertEqual(two_sum(self, nums=[3, 3], target=6), [0, 1])


# pair[7] = 0
# pair[2] = 1
def two_sum(self, nums: List[int], target: int) -> list:
    result = list()
    pairs = dict()
    for idx in range(0, len(nums)):
        num = nums[idx]
        if pairs.get(num) is not None:
            result = [pairs.get(num), idx]
            break
        pair = target - num
        pairs[pair] = idx
    return result


if __name__ == '__main__':
    unittest.main()
