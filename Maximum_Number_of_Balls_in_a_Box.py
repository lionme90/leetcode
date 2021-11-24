import unittest


#
# You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
#
# Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.
# 1 + 0 = 1.
# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

def digit_sum(num):
    return

def countBalls(self, lowLimit: int, highLimit: int) -> int:
    max_count = 0
    box_with_max_count = 0
    box_count = {}
    number_of_balls = highLimit - lowLimit + 1
    
    #
    ball_number = lowLimit
    while number_of_balls != 0:
        #calcualte box for each number
        # sum of digits in a loop
        box = sum([int(digit) for digit in str(ball_number)])
        if box_count.get(box):
            box_count[box] = box_count.get(box) + 1
        else:
            box_count[box] = 1
        #next number
        ball_number += 1
        number_of_balls -= 1

    # check if max count >= number of balls in the box
    for box in box_count:
        if max_count < box_count[box]:
            max_count = box_count[box]
    return max_count
    

class MyTestCase(unittest.TestCase):
    
    # Example 1:
    #
    # Input: lowLimit = 1, highLimit = 10
    # Output: 2
    # Explanation:
    # Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
    # Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
    # Box 1 has the most number of balls with 2 balls.
    
    def test_something(self):
        self.assertEqual(2, countBalls(self, 1, 10))
    
    # Example 2:
    #
    # Input: lowLimit = 5, highLimit = 15
    # Output: 2
    # Explanation:
    # Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
    # Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
    # Boxes 5 and 6 have the most number of balls with 2 balls in each.
    # Example 3:
    
    def test_something_2(self):
        self.assertEqual(2, countBalls(self, 5, 15))
    
    #
    # Input: lowLimit = 19, highLimit = 28
    # Output: 2
    # Explanation:
    # Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
    # Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
    # Box 10 has the most number of balls with 2 balls.
    def test_something_3(self):
        self.assertEqual(2, countBalls(self, 19, 28))


# Constraints:
#
# 1 <= lowLimit <= highLimit <= 10^5


if __name__ == '__main__':
    unittest.main()
