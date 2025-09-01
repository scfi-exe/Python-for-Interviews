# The deque in Python is actually a double-ended queue, meaning we can append or pop to either the left or right side
# appendleft() adds an element to the left side of the queue, while append() adds an element to the right side of the queue
# pop() removes and returns the rightmost element from the queue, and popleft() removes and returns the leftmost element from the queue

from typing import List, Deque
from collections import deque


# takes the list of integers, arr, and and integer, k. converts the list into a deque and rotates the values to the right by k steps
# return the resulting deque
def rotate_list(arr: List[int], k: int) -> Deque[int]:
    arrQue = deque(arr)
    for i in range(k):
        shifter = arrQue.pop()
        arrQue.appendleft(shifter)
    return arrQue


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
