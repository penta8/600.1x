import unittest
import getGuessedWord


class TestGetGuessedWord(unittest.TestCase):

    def testGetGuessedWord(self):
        tests = [['apple', ['e', 'i', 'k', 'p', 'r', 's'], '_ pp_ e'],
                 ['durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'],
                  'durian'],
                 ['banana', ['l', 'q', 'j', 'h', 'u', 'a', 'r', 'c', 'p', 'g'],
                  '_ a_ a_ a'],
                 ['coconut', ['p', 'y', 'e', 'z', 'l', 'w', 'h', 't',
                              'k', 'v'], '_ _ _ _ _ _ t'],
                 ['carrot', [], '_ _ _ _ _ _ '],
                 ['grapefruit', ['i', 'm', 'j', 'g', 'a', 'p', 't', 'l',
                                 'q', 'r'], 'grap_ _ r_ it']]
        for t in tests:
            self.assertEqual(getGuessedWord.getGuessedWord(t[0], t[1]), t[2])

if __name__ == '__main__':
    unittest.main()
