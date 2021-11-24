import unittest

# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
from typing import List


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        rotate(self, nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_something_2(self):
        nums = [-1, -100, 3, 99]
        rotate(self, nums, 2)
        self.assertEqual(nums, [3, 99, -1, -100])

    def test_something_22(self):
        nums = [-1, -100, 1, 1, 3, 3, 99]
        rotate(self, nums, 2)
        self.assertEqual(nums, [3, 99, -1, -100, 1, 1, 3])

    def test_something_3(self):
        nums = [1, 2]
        rotate(self, nums, 3)
        self.assertEqual(nums, [2, 1])

    def test_something_4(self):
        nums = [1, 2, 3, 4, 5, 6]

        rotate(self, nums, 11)
        self.assertEqual(nums, [2, 3, 4, 5, 6, 1])


if __name__ == '__main__':
    unittest.main()


def rotate2(self, nums: List[int], k: int) -> None:
    # swap first and last elements of array
    for i in range(0, k):
        tail_index = len(nums) - k + i
        nums[i], nums[tail_index] = nums[tail_index], nums[i]

    print(nums)

    tail_index = len(nums) - k
    index3 = 0
    # swapthje tail and rest of array
    for i in range(k, len(nums) - k):
        if tail_index < len(nums) - 1:
            nums[i], nums[tail_index] = nums[tail_index], nums[i]
            tail_index += 1
        else:
            nums[i], nums[len(nums) - index3] = nums[len(nums) + index3], nums[i]
            index3 += 1

            print(nums)


def rotate2(self, nums: List[int], k: int) -> None:
    # skip the full array rotations
    if k > len(nums):
        k = k % len(nums)
    # exit if no need to rotate, or just one element
    if k == 0 or len(nums) <= 1:
        return
    tail_copy = nums[len(nums) - k:]
    index = len(nums) - 1 - k
    while index >= 0:
        nums[index + k] = nums[index]
        index -= 1
    for i in range(0, len(tail_copy)):
        nums[i] = tail_copy[i]


def rotate(self, nums: List[int], k: int) -> None:
    # skip the full array rotations
    if k > len(nums):
        k = k % len(nums)
    # exit if no need to rotate, or just one element
    if k == 0 or len(nums) <= 1:
        return
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)


def reverse(nums: List[int], start, end: int):
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
