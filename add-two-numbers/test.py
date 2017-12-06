
import unittest
from link import ListNode
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        # call a function and get a value returned, and then assert the value
        # val = self.function_name()
        valReturned = 'a_value'
        valExpected = 'a_value'
        self.assertEqual(valReturned, valExpected)

    def test_add_two_numbers(self):
        return True


if __name__ == '__main__':
        print 'Testing class Solution...'
        unittest.main()

