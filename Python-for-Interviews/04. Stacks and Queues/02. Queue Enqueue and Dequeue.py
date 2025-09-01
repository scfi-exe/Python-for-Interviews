# a Queue is a data structure/list that follows a FIFO order
# 1. append() enqueues an element to the RIGHT side of the queue
# queue = deque()
# queue.append(1)  # [1]
# queue.append(2)  # [2]
# # 2. popleft() is used to remove and return the leftmost element from the queue
# queue = deque([1, 2])  # pass a list to initialize the queue
# queue.popleft()  # Returns 1, queue is now [2]
# queue.popleft()  # Returns 2, queue is now []
# # enqueue and dequeue are not built-into Python, so we must use collections.deque
# # 3.[0] and [-1] can be used to access the leftmost and rightmost elements of the queue, respectively. this assumes that the queue is not empty
# queue = deque([1, 2, 3, 4])
# leftmostElement = queue[0]  # 1
# rightmostElement = queue[-1]  # 4
# 4. We can use len() to check whether the queue is empty
# queue = deque([1,2])
# while len(queue)>0:
#     print(queue.popleft())

# === LESSON BEGINS BELOW ===
from typing import List, Deque
from collections import deque


# takes a list of integers arr, and an integer k
# should convert the list into a deque, then rotate the values in the list left by k steps and return the resulting deque
def rotate_list(arr: List[int], k: int) -> Deque[int]:
    arrQue = deque(arr)
    for i in range(k):
        shifter = arrQue.popleft()
        arrQue.append(shifter)
    return arrQue


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
