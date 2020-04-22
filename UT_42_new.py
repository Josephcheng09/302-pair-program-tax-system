import unittest
import taxsystem2

class Testtax42(unittest.TestCase):
# tax42(income of first person , income of second person)
# (Progressive tax - serperate , Stardard tax - joint , both standard rate , 1st Pro/2nd Std , 1st Std/2nd Pro)

    def test_tax42_1(self):
        self.assertEqual(taxsystem2.tax42(190000,190000) , (1940, 3820, 54150, 28045, 28045))
    def test_tax42_2(self):
        self.assertEqual(taxsystem2.tax42(190000,192000) , (1994, 3934, 54435, 28330, 28099))
    def test_tax42_3(self):
        self.assertEqual(taxsystem2.tax42(190000,292000) , (9510, 15146, 68685, 42580, 35615))
    def test_tax42_4(self):
        self.assertEqual(taxsystem2.tax42(190000,342000) , (15976, 23038, 75810, 49705, 42081))
    def test_tax42_5(self):
        self.assertEqual(taxsystem2.tax42(190000,392000) , (24110, 31385, 83175, 57070, 50215))
    def test_tax42_6(self):
        self.assertEqual(taxsystem2.tax42(190000,1228000) , (166230, 173505, 208575, 182470, 192335))
    def test_tax42_7(self):
        self.assertEqual(taxsystem2.tax42(192000,192000) , (2048, 4080, 54720, 28384, 28384))
    def test_tax42_8(self):
        self.assertEqual(taxsystem2.tax42(192000,292000) , (9564, 15412, 68970, 42634, 35900))
    def test_tax42_9(self):
        self.assertEqual(taxsystem2.tax42(192000,342000) , (16030, 23361, 76095, 49759, 42366))
    def test_tax42_10(self):
        self.assertEqual(taxsystem2.tax42(192000,392000) , (24164, 31708, 83460, 57124, 50500))
    def test_tax42_11(self):
        self.assertEqual(taxsystem2.tax42(192000,1228000) , (166284, 173828, 208860, 182524, 192620))
    def test_tax42_12(self):
        self.assertEqual(taxsystem2.tax42(292000,292000) , (17080, 31436, 83220, 50150, 50150))
    def test_tax42_13(self):
        self.assertEqual(taxsystem2.tax42(292000,342000) , (23546, 39511, 90345, 57275, 56616))
    def test_tax42_14(self):
        self.assertEqual(taxsystem2.tax42(292000,392000) , (31680, 47858, 97710, 64640, 64750))
    def test_tax42_15(self):
        self.assertEqual(taxsystem2.tax42(292000,1228000) , (173800, 189978, 223110, 190040, 206870))
    def test_tax42_16(self):
        self.assertEqual(taxsystem2.tax42(342000,342000) , (30012, 47586, 97470, 63741, 63741))
    def test_tax42_17(self):
        self.assertEqual(taxsystem2.tax42(342000,392000) , (38146, 55933, 104835, 71106, 71875))
    def test_tax42_18(self):
        self.assertEqual(taxsystem2.tax42(342000,1228000) , (180266, 198053, 230235, 196506, 213995))
    def test_tax42_19(self):
        self.assertEqual(taxsystem2.tax42(392000,392000) , (46280, 64280, 112200, 79240, 79240))
    def test_tax42_20(self):
        self.assertEqual(taxsystem2.tax42(392000,1228000) , (188400, 206400, 237600, 204640, 221360))
    def test_tax42_21(self):
        self.assertEqual(taxsystem2.tax42(1228000,1228000) , (330520, 348520, 363000, 346760, 346760))
    

if __name__ == '__main__':
    unittest.main()