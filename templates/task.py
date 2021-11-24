import unittest


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual(True, False)

    def test_something_2(self):
        self.assertEqual(True, False)

    def test_something_3(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
