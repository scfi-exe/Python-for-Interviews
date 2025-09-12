# Unfortunately, Python does not have a built-in max heap implementation.
# However, we can simulate a Max Heap by negating the values we insert into the heap
# This way, the element with the largest priority (the smallest value) will be at the top of the heap
# Then we can negate them back once they're ordered, to give us a positive value max heap

import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    maxHeap = []
    cleanHeap = []
    for num in nums:
        heapq.heappush(maxHeap, -num)

    # print(f"This is the maxHeap rn {maxHeap}")
    while maxHeap:
        top = -heapq.heappop(maxHeap)
        cleanHeap.append(top)
    return cleanHeap


# 1. we negated the numbers and pushed them onto the heap, which is technically implemented as a min heap
# 2. this way the largest number, 5, is at the top of the heap after being negated
# 3. We popped the elements from the heap and negated them back, to get the original numbers

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
