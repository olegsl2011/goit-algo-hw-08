import random
import unittest

from heap import *
from other import *


def random_unique_int_list(min_len, max_len, min_val, max_val):
    
    if min_len < 0 or max_len < min_len or min_val > max_val:
        raise ValueError("Invalid input parameters")

    length = random.randint(min_len, max_len)
    return random.sample(range(min_val, max_val), length)


class HeapMinCostOfJoiningTest(unittest.TestCase):

    def test_heap_and_sequential_joining_comparison(self):
        for i in range(100):
            cable_lengths = random_unique_int_list(1, 7, 1, 100)

            min_sequential_cost = min_cost_of_sequential_joining(cable_lengths)
            min_heap_cost = heap_min_cost_of_joining(cable_lengths)

            self.assertLessEqual(min_heap_cost["cost"], min_sequential_cost["cost"],
                                 f"Worst result at iteration {i}:\nCables lengths: {cable_lengths}\nHeap order: {min_heap_cost['order']}\nSequential order: {min_sequential_cost['order']}")

    def test_heap_and_paired_joining_comparison(self):
        for i in range(100):
            cable_lengths = random_unique_int_list(1, 7, 1, 100)

            min_paired_cost = min_cost_of_paired_joining(cable_lengths)
            min_heap_cost = heap_min_cost_of_joining(cable_lengths)

            self.assertLessEqual(min_heap_cost["cost"], min_paired_cost["cost"],
                                 f"Worst result at iteration {i}:\nCables lengths: {cable_lengths}\nHeap order: {min_heap_cost['order']}\nPaired order: {min_paired_cost['order']}")

    def test_heap_and_shortest_first_joining_comparison(self):
        for i in range(1000):
            cable_lengths = random_unique_int_list(1, 8, 1, 100)

            shortest_first_cost = cost_of_shortest_first_joining(cable_lengths)
            min_heap_cost = heap_min_cost_of_joining(cable_lengths)

            self.assertEqual(min_heap_cost, shortest_first_cost,
                             f"Not equal result at iteration {i}:\nCables lengths: {cable_lengths}\nHeap order: {min_heap_cost['order']}\nPaired order: {shortest_first_cost['order']}")


if __name__ == '__main__':
    unittest.main()
