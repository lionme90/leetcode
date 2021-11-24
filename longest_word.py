import re
import unittest


# Have the function LongestWord(sen) take the sen
# parameter being passed and return the longest word in the string.
# If there are two or more words that are the same length,
# return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty.
# Words may also contain numbers, for example "Hello world123 567"


# Examples
# Input: "fun&!! time"
# Output: time
# Input: "I love dogs"
# Output: love

class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual("time", longest_word("fun&!! time"))

    def test_something_2(self):
        self.assertEqual("love", longest_word("I love dogs"))

    def test_something_3(self):
        self.assertEqual("fun&!!time", longest_word("fun&!!time"))


def longest_word(sen: str):
    max_word_index = 0
    max_len = 0
    index = 0
    words = sen.split(" ")
    pattern = r'[^\w\s]'
    for word in words:
        mod_word = re.sub(pattern, '', word)
        if max_len < len(mod_word):
            max_len = len(mod_word)
            max_word_index = index
        index += 1
    return words[max_word_index]


if __name__ == '__main__':
    unittest.main()
