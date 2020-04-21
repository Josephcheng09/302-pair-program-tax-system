import unittest
import taxsystem2
import math

class Testtax41(unittest.TestCase):
# tax41(income of the single person)
# (tax under progressive tax , tax under stardard tax)

    def test_tax41_1(self):
        self.assertEqual(taxsystem2.tax41(150000) , (210, 21375))
    def test_tax41_2(self):
        self.assertEqual(taxsystem2.tax41(2100000) , (313500, 312300))
    def test_tax41_3(self):
        self.assertEqual(taxsystem2.tax41(250000) , (4550, 35625))
    def test_tax41_4(self):
        self.assertEqual(taxsystem2.tax41(520000) , (44900, 75300))
    def test_tax41_5(self):
        self.assertEqual(taxsystem2.tax41(1200000) , (160500, 177300))

if __name__ == '__main__':
    unittest.main()


