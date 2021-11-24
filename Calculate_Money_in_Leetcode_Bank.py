import unittest


# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
#
# He starts by putting in $1 on Monday, the first day.
# Every day from Tuesday to Sunday, he will put in $1 more than the day before.
# On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.


# Constraints:
#
# 1 <= n <= 1000


def totalMoneyO1(self, n: int) -> int:
    amount = 0


    
    # (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8 +9)
    #week = n of seq
    #seq =
    # calc weeks  7(1+7)/2 + 7(2+8)/2 + 7(3+9)/2
    #
    
    
    
    
    
    return amount
    

def totalMoney(self, n: int) -> int:
    if 0 > n > 1000:
        print("Not in a range")
        return 0
    amount = 0
    full_weeks = n // 7
    leftover_days = n % 7
    week = 1
    while week <= full_weeks:
        monday_step = week
        amount += monday_step
        for week_day in range(1, 7):
            monday_step += 1
            amount += monday_step
        week += 1
    monday_step = week
    if leftover_days > 0:
        amount += monday_step
        for _ in range(1, leftover_days):
            monday_step += 1
            amount += monday_step
    return amount
    

class MyTestCase(unittest.TestCase):

# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
    def test_something_1(self):
        self.assertEqual(10, totalMoney(self, 4))

# Input: n = 10
# Output: 37
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

    def test_something_2(self):
        self.assertEqual(37, totalMoney(self, 10))

# Input: n = 20
# Output: 96
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

    def test_something_3(self):
        self.assertEqual(96, totalMoney(self, 20))


if __name__ == '__main__':
    unittest.main()
