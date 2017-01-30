import unittest
from getAvLetters import getAvailableLetters


class TestGetAvLetters(unittest.TestCase):
    def test_getAvailableLetters(self):
        tests = [{'argument': ['e', 'i', 'k', 'p', 'r', 's'],
                  'result': 'abcdfghjlmnoqtuvwxyz'},
                 {'argument': [],
                  'result': 'abcdefghijklmnopqrstuvwxyz'},
                 {'argument': ['h', 's', 'b', 'y', 'q', 'e',
                               't', 'o', 'd', 'k', 'n', 'l'],
                  'result': 'acfgijmpruvwxz'},
                 {'argument': ['k', 's', 'u', 'y', 'e', 'r',
                               'f', 'l', 'x', 't', 'w'],
                  'result': 'abcdghijmnopqvz'},
                 {'argument': ['r', 'e', 'i', 'w', 'd'],
                  'result': 'abcfghjklmnopqstuvxyz'},
                 {'argument': ['u', 'i', 'q', 'l', 'v'],
                  'result': 'abcdefghjkmnoprstwxyz'}]

        for t in tests:
            self.assertEqual(getAvailableLetters(t['argument']), t['result'])


if __name__ == '__main__':
    unittest.main()
