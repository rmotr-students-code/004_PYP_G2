# Write a function that receives two numbers and an operation name and returns the correct value

# Instructions:
# Input: 'sum', 2, 3
# <function>
# Output: 5

def calculator(operation, num1, num2):
    
    if operation == 'sum':
        return num1 + num2
    elif operation == 'subtraction':
        return num1 - num2
        
        
        


import unittest

class BasicCalculatorTestCase(unittest.TestCase):
    def test_calculator_add(self):
        result = calculator('sum', 2, 3)
        self.assertEqual(result, 5)

    def test_calculator_subtract(self):
        result = calculator('subtraction', 7, 5)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()