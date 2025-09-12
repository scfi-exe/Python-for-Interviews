# Unfortunately, Python also does not have a customer KEY parameter for the HEAPQ module
# This means we cannot directly create a heap with custom priorities
# However, we can *simulate* a custom heap by using a TUPLE as the element as the element in the heap

# with TUPLES, Python will use the FIRST element as the priority
# If two TUPLES have the same first element, Python will compare the SECOND element as priority, and so on
# [think, alphabetical?]

# If we wanted to create a heap of integers by using the absolute value of each integer as the priority,
# we could use the following code:
# import heapq

# nums = [4, -2, 3, -5]
# heap = []

# for num in nums:
#     pair = (abs(num), num)
#     heapq.heappush(heap, pair)

# while heap:
#     pair = heapq.heappop(heap)
#     original_num = pair[1]
#     print(original_num)

# 1. we pushed tuples onto the the heap where the first element was the absolute value and the second element was the original #
# 2. the heap was a MIN HEAP based on the first element of each tuple
# 3. we popped the tuples and printed the second element from each, which was the original number


import heapq
from typing import List


# takes a list of integers and returns the integers in reverse sorted order.
# you should use the above tuple technique to achieve this
def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    for num in nums:
        pair = (abs(num), num)
        heapq.heappush(heap, pair)
    output = []
    while heap:
        pair = heapq.heappop(heap)
        output.append(pair[1])
    return output


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
