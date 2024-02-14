import unittest
import random
import count_sort

class TestCountingSort(unittest.TestCase):
    def random_array(self, min_size, max_size, value_range):
        size = random.randint(min_size, max_size)
        return [random.randint(*value_range) for _ in range(size)]

    def test_empty_array(self):
        self.assertEqual(count_sort.count_sort([], 1000), [], "Failed on empty array")

    def test_random_positive_without_zero(self):
        arr = self.random_array(10, 1000, (1, 1000))
        self.assertEqual(count_sort.count_sort(arr, 1000), sorted(arr), "Failed on random positive integers without zero")

    def test_random_positive_with_zero(self):
        arr = self.random_array(10, 1000, (0, 1000))
        self.assertEqual(count_sort.count_sort(arr, 1000), sorted(arr), "Failed on random positive integers with zero")

    def test_sorted_positive_with_zero(self):
        arr = sorted(self.random_array(10, 1000, (0, 1000)))
        self.assertEqual(count_sort.count_sort(arr, 1000), arr, "Failed on sorted positive integers with zero")

    def test_random_integers(self):
        arr = self.random_array(10, 1000, (-100, 100))
        self.assertEqual(count_sort.count_sort(arr, 1000), sorted(arr), "Failed on random integers")

if __name__ == '__main__':
    unittest.main()
