from typing import List
from sortedcontainers import SortedSet


# takes a sorted set of integers, SortedSet, and two lists of integers, num1 and num2
# the elements from num1 should be added to the sorted set
# then, the elements from num2 should be removed from the sorted set
# finally, return the first 3 elements of the sorted set
def get_first_three(
    sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]
) -> List[int]:
    for num in nums1:
        sorted_set.add(num)
    for num in nums2:
        sorted_set.discard(num)
    return sorted_set[0:3]


# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(
    get_first_three(
        SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]),
        [10, 11, 12],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    )
)
