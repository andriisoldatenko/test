import unittest
import random


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers1(self):
        self.assertEqual(12, 12)

    def test_numbers2(self):
        self.assertEqual(12, 12)

    def test_numbers3(self):
        self.assertEqual(12, 12)

    def test_numbers4(self):
        self.assertEqual(12, 12)

    def test_numbers5(self):
        self.assertEqual(12, 12)

    def test_numbers6(self):
        self.assertEqual(12, 12)

    def test_numbers7(self):
        self.assertEqual(12, 12)

    def test_numbers8(self):
        self.assertEqual(12, 12)

    def test_numbers9(self):
        self.assertEqual(12, 12)

    def test_numbers10(self):
        self.assertEqual(12, 12)

    def test_numbers11(self):
        self.assertEqual(12, random.randint(11, 13))

    def test_numbers12(self):
        self.assertEqual(12, random.randint(11, 12))

if __name__ == '__main__':
    unittest.main()
