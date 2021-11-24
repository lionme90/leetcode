import unittest


# mergeSortedArrays([0,3,4,31], [3,4,6,30]);
#

def merge_sorted(one, two: list) -> list:
    if len(one) == 0:
        return two
    if len(two) == 0:
        return one
    result = []
    result_index = 0
    index1 = 0
    index2 = 0
    while len(one) > index1 and len(two) > index2:
        if one[index1] < two[index2]:
            result.append(one[index1])
            index1 += 1
        else:
            result.append(two[index2])
            index2 += 1
        result_index += 1

    while len(one) > index1:
        result.append(one[index1])
        index1 += 1
        result_index += 1
    while len(two) > index2:
        result.append(two[index2])
        index2 += 1
        result_index += 1
    return result


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual(merge_sorted([0, 3, 4, 31], [3, 4, 6, 30]), [0, 3, 3, 4, 4, 6, 30, 31])


if __name__ == '__main__':
    unittest.main()
