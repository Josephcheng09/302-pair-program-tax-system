import unittest
import taxsystem2

class Testtax42(unittest.TestCase):
# tax42(income of first person , income of second person)
# (Progressive tax - serperate , Stardard tax - joint , both standard rate , 1st Pro/2nd Std , 1st Std/2nd Pro)

    def test_tax42_1(self):
        self.assertEqual(taxsystem2.tax42(150000,180000) , (990, 990, 47025, 25860, 22155))
    def test_tax42_2(self):
        self.assertEqual(taxsystem2.tax42(1200000,10000) , (160500, 139760, 178800, 162000, 177300))
    def test_tax42_3(self):
        self.assertEqual(taxsystem2.tax42(1500000,12280000) , (2255600, 2273600, 2061600, 2050800, 2266400))
    

if __name__ == '__main__':
    unittest.main()