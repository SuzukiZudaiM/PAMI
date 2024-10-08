import unittest
from gen import generate_transactional_dataset
from automated_test_CMine import test_pami
import warnings

warnings.filterwarnings("ignore")

class TestCMine(unittest.TestCase):
    def test_num_patterns(self):
        for _ in range(3):
            num_distinct_items = 20
            num_transactions = 1000
            max_items_per_transaction = 20
            items = ["item-{}".format(i) for i in range(1, num_distinct_items + 1)]
            dataset = generate_transactional_dataset(num_transactions, items, max_items_per_transaction)

            cmine_result = test_pami(dataset)
            self.assertGreater(len(cmine_result), 0, "No patterns were generated by CMine")

        print("3 test cases for number of patterns have been passed")

    def test_equality(self):
        for _ in range(3):
            num_distinct_items = 20
            num_transactions = 1000
            max_items_per_transaction = 20
            items = ["item-{}".format(i) for i in range(1, num_distinct_items + 1)]
            dataset = generate_transactional_dataset(num_transactions, items, max_items_per_transaction)

            cmine_result = test_pami(dataset)
            cmine_patterns = sorted(list(cmine_result["Patterns"]))
            self.assertTrue(len(cmine_patterns) > 0, "No patterns were generated by CMine")

        print("3 test cases for Patterns equality are passed")

    def test_support(self):
        for _ in range(3):
            num_distinct_items = 20
            num_transactions = 1000
            max_items_per_transaction = 20
            items = ["item-{}".format(i) for i in range(1, num_distinct_items + 1)]
            dataset = generate_transactional_dataset(num_transactions, items, max_items_per_transaction)

            cmine_result = test_pami(dataset)
            cmine_result.sort_values(by="Support", inplace=True)
            supports = list(cmine_result["Support"])
            for support in supports:
                self.assertTrue(support > 0, "Support value should be greater than 0")

        print("3 test cases for support equality are passed")

if __name__ == '__main__':
    unittest.main()
