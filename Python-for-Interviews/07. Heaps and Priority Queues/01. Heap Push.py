import heapq
from typing import List


def heap_push(heap: List[int], value: int) -> int:
    output = []
    for i in heap:
        heapq.heappush(output, i)
    return output[0]


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
