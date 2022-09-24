import unittest
from MyVersion.vector import Vector

class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)

    def test_magnitude(self):
        self.assertEqual(self.v1.getMagnitude(), 3)


if __name__ == "__main__":
    unittest.main()
