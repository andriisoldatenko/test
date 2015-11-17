import unittest
import random

def generate_number():
    pdf = [(12, 0.9), (11, 0.05), (13, 0.05)]
    cdf = [(i, sum(p for j,p in pdf if j < i)) for i,_ in pdf]
    R = max(i for r in [random.random()] for i,c in cdf if c <= r)
    return R


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
        self.assertEqual(12, generate_number())

    def test_numbers12(self):
        self.assertEqual(12, generate_number())


class TestUM1(unittest.TestCase):

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
        self.assertEqual(12, generate_number())


class TestUM2(unittest.TestCase):

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
        self.assertEqual(12, generate_number())

    def test_numbers12(self):
        self.assertEqual(12, generate_number())


if __name__ == '__main__':
    unittest.main()

