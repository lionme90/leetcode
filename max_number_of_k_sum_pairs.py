import unittest

# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.
from typing import List


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual(2, maxOperations(self, [1, 2, 3, 4], 5))

    def test_something_2(self):
        self.assertEqual(1, maxOperations(self, [3, 1, 3, 4, 3], 6))

    def test_something_3(self):
        self.assertEqual(2, maxOperations(self, [2, 2, 2, 3, 1, 1, 4, 1], 4))

    def test_something_4(self):
        self.assertEqual(2, maxOperations(self, [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2))

    def test_something_5(self):
        self.assertEqual(4, maxOperations(self, [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3))


def maxOperations(self, nums: List[int], k: int) -> int:
    pairs = dict()
    result = 0
    for num in nums:
        if pairs.get(num, 0) > 0:
            # pair found from previous calculation
            result += 1
            pairs[num] = pairs[num] - 1
        else:
            pair = k - num
            pairs[pair] = pairs.get(pair, 0) + 1
    return result


if __name__ == '__main__':
    unittest.main()
