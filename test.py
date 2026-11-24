import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()


"""
The test checks if the sum function adds numbers correctly, as the
example shows above. This test shows that the sum function is working correctly.
"""