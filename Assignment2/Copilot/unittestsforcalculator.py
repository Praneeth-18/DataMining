# write unit test cases for calculator.py

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1, -1), 1)
        self.assertEqual(calculator.divide(5, 2), 2.5)
        
        #self.assertRaises(ValueError, calculator.divide, 10, 0)
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)
    
    def test_sin(self):
        self.assertEqual(calculator.sin(0), 0)
        self.assertEqual(calculator.sin(90), 1)
        self.assertEqual(calculator.sin(180), 0)
        self.assertEqual(calculator.sin(270), -1)
        self.assertEqual(calculator.sin(360), 0)
        self.assertEqual(calculator.sin(45), 0.7071067811865475)
        self.assertEqual(calculator.sin(30), 0.49999999999999994)
        self.assertEqual(calculator.sin(60), 0.8660254037844386)
        self.assertEqual(calculator.sin(120), 0.8660254037844386)
        self.assertEqual(calculator.sin(150), 0.49999999999999994)
        self.assertEqual(calculator.sin(210), -0.49999999999999994)
        self.assertEqual(calculator.sin(240), -0.8660254037844386)
        self.assertEqual(calculator.sin(300), -0.8660254037844386)
        self.assertEqual(calculator.sin(330), -0.49999999999999994)


if __name__ == '__main__':
    unittest.main()