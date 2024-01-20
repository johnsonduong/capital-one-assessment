import unittest

from rules_engine import calculate_max_points
from helper import read_transactions_from_file
from rules import RULES

class TestCalculateMaxPoints(unittest.TestCase):
    # A test case class for testing the calculate_max_points function.

    def setUp(self):
        """Load transactions from file once for all tests."""
        self.transactions_example123 = read_transactions_from_file('transactions/example123.json')
        self.transactions_example4 = read_transactions_from_file('transactions/example4.json')

    def test_no_transactions(self):
        transactions = {}
        rules = [
            {
                'points': 1,
                'requirements': {'all': 100}
            }
        ]
        expected_result = 0
        self.assertEqual(calculate_max_points(transactions, rules), expected_result)

    def test_example1(self):
        rules = [
            {
                'points': 10,
                'requirements': {'sportcheck': 1}
            }
        ]
        expected_result = 730
        self.assertEqual(calculate_max_points(self.transactions_example123, rules), expected_result)

    def test_example2(self):
        rules = [
            {
                'points': 10,
                'requirements': {'sportcheck': 1}
            },
            {
                'points': 100,
                'requirements': {'sportcheck': 5}
            },
        ]
        expected_result = 1430
        self.assertEqual(calculate_max_points(self.transactions_example123, rules), expected_result)

    def test_example3(self):
        rules = [
            {
                'points': 100,
                'requirements': {'sportcheck': 5}
            },
            {
                'points': 10,
                'requirements': {'all': 1}
            },
        ]
        expected_result = 1560
        self.assertEqual(calculate_max_points(self.transactions_example123, rules), expected_result)

    def test_example4(self):
        rules = RULES
        expected_result = 95
        self.assertEqual(calculate_max_points(self.transactions_example4, rules), expected_result)

if __name__ == '__main__':
    unittest.main()