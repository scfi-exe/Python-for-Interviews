# heaps (or priority queues) are a data structure that allow you to push (insert) and pop (remove) elements based on some priority associated w each element
# in python, a heap is a MINIMUM heap by DEFAULT, meaning that the element with the smallest priority is always at the top of the heap
# import heapq

# heap = [] # min heap

# heapq.heappush(heap, 3)
# heapq.heappush(heap, 1)

# print(heap[0])  # 1

# heapq.heappush(heap, 0)

# print(heap[0])  # 0
# 1. we first imported the heapq module, which contains functions for working with heaps
# 2. we created an empty list called heap. heaps are implemented as LISTS in Python
# 3. we pushed elements 3 and 1 into the heap
# 4. we printed the element with the smallest priority at the top of the heap, heap[0] whose value was 1
#    the element with the smallest priority is always at index 0, this is the same as calling .top() in other languages
# 5. we pushed the element 0 into the heap
# 6. we accessed the element with the smallest priority, which is now 0

import heapq
from typing import List


# pushes the integer, value, onto the heap, heap.
# the heap should be a min heap, meaning that the element with the smallest priority returns at index 0
# after pushing the element, return the element with the smallest priority in the heap
def heap_push(heap: List[int], value: int) -> int:
    heapq.heappush(heap, value)
    return heap[0]


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
