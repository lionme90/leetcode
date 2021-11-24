import unittest

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.


# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Input: nums = [0]
# Output: [0]
from typing import List

from templates.algo_snippets import swap


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        nums = [0, 1, 0, 3, 12]
        move_zeroes(self, nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_something_2(self):
        nums = [0]
        move_zeroes(self, nums)
        self.assertEqual(nums, [0])


if __name__ == '__main__':
    unittest.main()


def move_zeroes2(self, nums: List[int]) -> None:
    index = 0
    swaps_indexes = set()
    for n in nums:
        if n == 0:
            swaps_indexes.add(index)
        else:
            if len(swaps_indexes) > 0:
                index_to_swap = swaps_indexes.pop()
                nums[index_to_swap] = n
                nums[index] = 0
                swaps_indexes.add(index)
        index += 1


def move_zeroes(self, nums: List[int]) -> None:
    index = 0
    index_non_zero = 0
    for n in nums:
        if n != 0:
            swap(index, index_non_zero, nums)
            index_non_zero += 1
        index += 1
