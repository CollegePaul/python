import unittest

from area import area

class TestArea(unittest.TestCase):

    def test_standard(self):
        result= area(4,5)
        self.assertEqual(result, 20)

    def test_zero(self):
        result= area(4,0)
        self.assertEqual(result, 0)

    def test_decimal(self):
        result= area(4.3,2.2)
        self.assertEqual(result, 9.46)

    def test_string(self):
        result= area("a","b")
        self.assertEqual(result, "Error: must be a number")

    def test_negative(self):
        result= area(-4,5)
        self.assertEqual(result, "Error: Must be postive")

    
    def test_binary(self):
        result = area(0b101,0b111)
        self.assertEqual(result, 35)

    def test_complex(self):
        result= area(1.5 * 2j, 4)
        self.assertEqual(result, 12j)




if __name__ == '__main__':
    unittest.main()
