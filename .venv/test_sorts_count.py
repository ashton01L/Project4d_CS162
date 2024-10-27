# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/26/2024
# Description: Write a bubble sort that counts the number of comparisons and the number of exchanges made while sorting
# a list and returns a tuple of the two values (comparisons first, exchanges second). Do the same for insertion sort.
import unittest

from sorts_count import bubble_count, insertion_count


class TestSortCounts(unittest.TestCase):

    def test_bubble_count_random_order(self):
        a_list = [5, 3, 1, 4, 2]
        expected_sorted = [1, 2, 3, 4, 5]

        # Call bubble_count on a copy of the list and check the sorted copy
        sorted_list = a_list.copy()
        bubble_comparisons, bubble_exchanges = bubble_count(sorted_list)

        # Assert sorted list is correct and count values
        self.assertEqual(sorted_list, expected_sorted)
        self.assertEqual(bubble_comparisons, 10)  # Adjust based on count logic
        self.assertEqual(bubble_exchanges, 7)  # Adjust based on count logic

    def test_insertion_count_random_order(self):
        a_list = [5, 3, 1, 4, 2]
        expected_sorted = [1, 2, 3, 4, 5]

        # Call insertion_count on a copy of the list and check the sorted copy
        sorted_list = a_list.copy()
        insertion_comparisons, insertion_exchanges = insertion_count(sorted_list)

        # Assert sorted list is correct and count values
        self.assertEqual(sorted_list, expected_sorted)
        self.assertEqual(insertion_comparisons, 9)  # Adjust based on count logic
        self.assertEqual(insertion_exchanges, 7)  # Adjust based on count logic

    def test_bubble_count_sorted(self):
        a_list = [1, 2, 3, 4, 5]
        expected_sorted = [1, 2, 3, 4, 5]

        sorted_list = a_list.copy()
        bubble_comparisons, bubble_exchanges = bubble_count(sorted_list)

        # List should remain sorted, with no exchanges
        self.assertEqual(sorted_list, expected_sorted)
        self.assertEqual(bubble_comparisons, 10)  # Based on fully sorted list comparisons
        self.assertEqual(bubble_exchanges, 0)

    def test_insertion_count_sorted(self):
        a_list = [1, 2, 3, 4, 5]
        expected_sorted = [1, 2, 3, 4, 5]

        sorted_list = a_list.copy()
        insertion_comparisons, insertion_exchanges = insertion_count(sorted_list)

        # List should remain sorted, with no exchanges
        self.assertEqual(sorted_list, expected_sorted)
        self.assertEqual(insertion_comparisons, 4)  # 1 per element after the first
        self.assertEqual(insertion_exchanges, 0)

    def test_bubble_count_reverse_sorted(self):
        a_list = [5, 4, 3, 2, 1]
        expected_sorted = [1, 2, 3, 4, 5]

        sorted_list = a_list.copy()
        bubble_comparisons, bubble_exchanges = bubble_count(sorted_list)

        # Check if the list is correctly sorted and counts are as expected
        self.assertEqual(sorted_list, expected_sorted)
        self.assertEqual(bubble_comparisons, 10)  # Adjust based on count logic
        self.assertEqual(bubble_exchanges, 10)  # Adjust based on count logic

    def test_insertion_count_reverse_sorted(self):
        a_list = [5, 4, 3, 2, 1]
        expected_sorted = [1, 2, 3, 4, 5]

        sorted_list = a_list.copy()
        insertion_comparisons, insertion_exchanges = insertion_count(sorted_list)

        # Check if the list is correctly sorted and counts are as expected
        self.assertEqual(sorted_list, expected_sorted)
        self.assertEqual(insertion_comparisons, 10)
        self.assertEqual(insertion_exchanges, 10)

    def test_bubble_count_with_duplicates(self):
        a_list = [3, 3, 1, 2, 2]
        expected_sorted = [1, 2, 2, 3, 3]

        sorted_list = a_list.copy()
        bubble_comparisons, bubble_exchanges = bubble_count(sorted_list)

        self.assertEqual(sorted_list, expected_sorted)
        # Adjust counts based on count logic with duplicates
        # self.assertEqual(bubble_comparisons, ...)
        # self.assertEqual(bubble_exchanges, ...)

    def test_insertion_count_with_duplicates(self):
        a_list = [3, 3, 1, 2, 2]
        expected_sorted = [1, 2, 2, 3, 3]

        sorted_list = a_list.copy()
        insertion_comparisons, insertion_exchanges = insertion_count(sorted_list)

        self.assertEqual(sorted_list, expected_sorted)
        # Adjust counts based on count logic with duplicates
        # self.assertEqual(insertion_comparisons, ...)
        # self.assertEqual(insertion_exchanges, ...)


# Run the tests
if __name__ == '__main__':
    unittest.main()
