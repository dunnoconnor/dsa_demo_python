import unittest
from mergeSort import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_sorted_array(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_array_with_negative_numbers(self):
        self.assertEqual(merge_sort([-5, -1, -4, 2, 0]), [-5, -4, -1, 0, 2])

    def test_array_with_duplicates(self):
        self.assertEqual(merge_sort([5, 5, 3, 3, 1, 1]), [1, 1, 3, 3, 5, 5])

if __name__ == "__main__":
    unittest.main()