#unit testing

#My area function (accurate to 9 dp)
def areaOfSquare(sideLength):
    area = sideLength*sideLength
    area = round(area,9)
    return area


#tests
import unittest

class TestArea(unittest.TestCase):
    def test_number(self):
        result = areaOfSquare(4)
        self.assertEqual(result, 16)

    def test_zero(self):
        result = areaOfSquare(0)
        self.assertEqual(result, 0)
    
    def test_decimal(self):
        result = areaOfSquare(0.2)
        self.assertEqual(result, 0.04)

    def test_negative(self):
        result = areaOfSquare(-1.3)
        self.assertEqual(result, 1.69)   

    def test_large(self):
        result = areaOfSquare(58209890482903840923)
        self.assertEqual(result, 3388391350031659154606776518186089491929)   
        
    def test_complex(self):
        result = areaOfSquare(2 + 2j)
        self.assertEqual(result, 8j)



if __name__ == '__main__':
    unittest.main()  


