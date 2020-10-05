import unittest

# from class import method or methods

class testMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum([5, 2]), 7)

    def test2(self):
        self.assertEqual(sum([3, 2]), 7)


if __name__ == '__main__':
    unittest.main()