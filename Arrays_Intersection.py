import unittest


# Given 2 arrays, create a function that let's a user know ()true /false whether this two arrays contain
# any common items
# For example:
# const array1 = ['a', 'b', 'c', 'x']
# const array2 = ['z', 'y', 'i']
# should return false
# -------
# const array1 = ['a', 'b', 'c', 'x']
# const array2 = ['z', 'y', 'x']
# should return true

# 2 parameters - arrays , return boolean

# s1 nested for loops O(a*b), code is not efficient
# s2, put items from first array int a set and, check of values from second array exists there O(a+b)


def contains_intersection(array1, array2: []) -> bool:
    memo = set()
    for item in array1:
        memo.add(convert(item))

    for item in array2:
        if convert(item) in memo:
            return True
    return False


def convert(item):
    if isinstance(item, list):
        return tuple(item)
    return item


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        array1 = ['a', None, 'c', 'x']
        array2 = ['z', None, 'x']
        self.assertEqual(True, contains_intersection(array1, array2))

    def test_something_2(self):
        array1 = ['a', 'b', 'c', 'x']
        array2 = ['z', 'y', 'i']
        self.assertEqual(False, contains_intersection(array1, array2))

    def test_something_3(self):
        array1 = ['a', 'b', 'c', []]
        array2 = ['z', 'y', []]
        self.assertEqual(True, contains_intersection(array1, array2))


if __name__ == '__main__':
    unittest.main()
