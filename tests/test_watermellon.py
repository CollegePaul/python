#4a watermellon 800
#https://codeforces.com/problemset/problem/4/AS

#this is a demo and will not pass the codeforces test.S

#y = int(input())
#dont forget all returns should be print when uploading
def watermellon(y):   
   if y==8:
       return "YES"


#tests
import unittest

class TestWatermellon(unittest.TestCase):
    def test_1(self):
     
        result = watermellon(8)
        self.assertEqual(result, "YES")



if __name__ == '__main__':
    unittest.main()