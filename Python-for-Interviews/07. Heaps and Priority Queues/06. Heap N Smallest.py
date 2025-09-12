# Heaps provide a very convenient way to find the smallest elements in a collection
# For this, we can use heapq.nmallest()

import heapq
from typing import List


# returns the smallest element in a heap
def get_min_element(arr: List[int]) -> int:
    output = heapq.nsmallest(1, arr)
    return output[0]


# returns the smallest 4 elements in a heap
def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    return heapq.nsmallest(4, arr)


# returns the smallest 2 element sin a heap
def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    output = heapq.nsmallest(2, arr)
    output.sort(reverse=True)
    return output


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))
