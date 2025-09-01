# Python does not have a built-in stack data structure, but we can use a list to achieve the same purposes
# A stack is basically a LIFO list (so, reversed)
# 1. append() is used to push an element onto the stack
stack = []
stack.append(1)
stack.append(2)
# 2. pop() is used to remove and return the element from the top (rightmost) item in the stack
stack = [1, 2]
top_element = stack.pop()  # 2
# 3. [-1] can be used to access the top-most (rightmost) element in the stack without removing it
#    this assumes that the stack is not empty
stack = [1, 2]
top_element = stack[-1]  # 2
# 4. len() can be used to check if the stack is empty
# stack = [1, 2]
# while len(stack) > 0:
#     print(stack.pop())


# CHALLENGE BEGINS BELOW
from typing import List

# This code works but it's not what the challenge is asking for so I'm commenting it out
# def reverse_list(arr: List[int]) -> List[int]:
#     return arr[::-1]


def reverse_list(arr: List[int]) -> List[int]:
    reverseArr = []
    while len(arr) > 0:
        reverseArr.append(arr.pop())
    return reverseArr


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
