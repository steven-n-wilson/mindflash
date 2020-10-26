from card import card
import unittest

# from class import method or methods

class testMethods(unittest.TestCase):    
    def test1(self): # width
        testCard = card(200, 100, "white", "arial", "frontside text", "backside text", "placeholder url")
        self.assertEqual(testCard.width, 200)

    def test2(self):
        testCard = card(200, 100, "white", "arial", "frontside text", "backside text", "placeholder url")
        self.assertEqual(testCard.height, 100)
    
    def test3(self):
        testCard = card(200, 100, "white", "arial", "frontside text", "backside text", "placeholder url")
        self.assertEqual(testCard.color, "white")
    
    def test4(self):
        testCard = card(200, 100, "white", "arial", "frontside text", "backside text", "placeholder url")
        self.assertEqual(testCard.font, "arial")

    def test5(self):
        testCard = card(200, 100, "white", "arial", "frontside text", "backside text", "placeholder url")
        self.assertEqual(testCard.front, "frontside text")

    def test6(self):
        testCard = card(200, 100, "white", "arial", "frontside text", "backside text", "placeholder url")
        self.assertEqual(testCard.back, "backside text")
    
    def test7(self):
        testCard = card(200, 100, "white", "arial", "frontside text", "backside text", "placeholder url")
        self.assertEqual(testCard.media_f, "placeholder url")

if __name__ == '__main__':
    unittest.main()