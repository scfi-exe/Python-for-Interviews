# We can also remove elements using the heapq.heappop(heap) function
# this function removes the element with the SMALLEST PRIORITY and returns it's value


import heapq
from typing import List


# pops all of the elements from a heap and returns them in a list in the order in which they were popped
# the heap should be a min heap, meaning that the elements with the smallest priority should be popped first.
def heap_pop(heap: List[int]) -> List[int]:
    output = []
    for i in range(len(heap)):
        output.append(heapq.heappop(heap))
    return output


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
