# if we are given a list of elements upfront, we can convert them into a HEAP using the heapq.heapify(list) function
# this function rearranges the elements of the list so that they form a valid heap
# the heap is minimum by default, meaning that the element with the smallest priority will be at index 0

# CHALLENGE
import heapq
from typing import List


# takes a list of strings and returns a list of strings that have been transformed into a min heap
def heapify_strings(strings: List[str]) -> List[str]:
    heapq.heapify(strings)
    return strings


# takes a list of integers and returns a list of integers that have been transformed into a min heap
def heapify_integers(integers: List[int]) -> List[int]:
    heapq.heapify(integers)
    return integers


# takes a list of integers and returns a list of integers that have been sorted in ASCENDING order
# you should use the heapify function to transform the list into a heap before sorting it
def heap_sort(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    nums.sort()
    return nums


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
