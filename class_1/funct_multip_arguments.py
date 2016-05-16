
def calculator_sum(*nums):
    count = 0
    for num in nums:
        count += num
    return count


def calculator_subtraction(*nums):
    count = nums[0]
        
    for num in range(len(nums) - 1):
        count -= nums[num + 1]
    return count


def calculator(operation, *nums):
    if operation == 'sum':
        return calculator_sum(*nums)

    elif operation == 'subtraction':
        return calculator_subtraction(*nums)
    else: 
        raise AttributeError


import unittest

class BasicCalculatorTestCase(unittest.TestCase):
    def test_calculator_add(self):
        result = calculator('sum', 2, 3)
        self.assertEqual(result, 5)

    def test_calculator_subtract_two_numbers(self):
        result = calculator('subtraction', 7, 5)
        self.assertEqual(result, 2)
        
    def test_calculator_subtract_one_numbers(self):
        result = calculator('subtraction', 7)
        self.assertEqual(result, 7)
        
    def test_calculator_subtract_four_numbers(self):
        result = calculator('subtraction', 11, 1, 2, 3)
        self.assertEqual(result, 5)
        
    def test_invalid_operation_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            calculator('invalid-op!', 7, 5)
            
    def test_sum_with_one_number(self):
        result = calculator('sum', 1)
        self.assertEqual(result, 1)
        
    def test_sum_with_two_numbers(self):
        result = calculator('sum', 2, 3)
        self.assertEqual(result, 5)

    def test_sum_with_four_numbers(self):
        result = calculator('sum', 2, 3, 5, 7)
        self.assertEqual(result, 17)


if __name__ == '__main__':
    unittest.main()