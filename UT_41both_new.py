import unittest
import taxsystem2
import math

class Testtax41(unittest.TestCase):
# tax41(income of the single person)
# (tax under progressive tax , tax under stardard tax)

    def test_tax41_1(self):
        self.assertEqual(taxsystem2.tax41(85200) , (0, 12141))
    def test_tax41_2(self):
        self.assertEqual(taxsystem2.tax41(132000) , (0, 18810))
    def test_tax41_3(self):
        self.assertEqual(taxsystem2.tax41(190000) , (970, 27075))
    def test_tax41_4(self):
        self.assertEqual(taxsystem2.tax41(192000) , (1024, 27360))
    def test_tax41_5(self):
        self.assertEqual(taxsystem2.tax41(242000) , (3874, 34485))
    def test_tax41_6(self):
        self.assertEqual(taxsystem2.tax41(292000) , (8540, 41610))
    def test_tax41_7(self):
        self.assertEqual(taxsystem2.tax41(342000) , (15006, 48735))
    def test_tax41_8(self):
        self.assertEqual(taxsystem2.tax41(392000) , (23140, 56100))
    def test_tax41_9(self):
        self.assertEqual(taxsystem2.tax41(1228000) , (165260, 181500))    

if __name__ == '__main__':
    unittest.main()


