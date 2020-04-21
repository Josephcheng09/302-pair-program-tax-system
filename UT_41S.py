import unittest
import taxsystem1

class Testtax41_S(unittest.TestCase):

    def test_tax41_1(self):
        self.assertEqual(taxsystem1.tax41_S(150000) , 21375)
    def test_tax41_2(self):
        self.assertEqual(taxsystem1.tax41_S(2100000) , 312300)
    def test_tax41_3(self):
        self.assertEqual(taxsystem1.tax41_S(4500000) , 210)
    def test_tax41_4(self):
        self.assertEqual(taxsystem1.tax41_S(120000) , 210)

if __name__ == '__main__':
    unittest.main()