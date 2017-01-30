import unittest
import isWordGuessed


class TestIsWordGuessed(unittest.TestCase):
    def test_function(self):
        tests = [['apple',  ['a', 'e', 'i', 'k', 'p', 'r', 's'], False],
                 ['durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'],
                  True]]
        for t in tests:
            self.assertEqual(isWordGuessed.isWordGuessed(t[0], t[1]), t[2])

if __name__ == '__main__':
    unittest.main()
