from typing import List


def swap(i, j, array: List):
    array[i], array[j] = array[j], array[i]
    return array
