# It is common to make a copy of a list in many algorithms. Python provides multiple ways to do it. Here are a few:
# 1. Using the copy() method:
original_list = [1, 2, 3]
cloned_list = original_list.copy()
# 2. Using the slicing syntax:
original_list = [1, 2, 3]
cloned_list = original_list[:]
# 3. Using the list() constructor
original_list = [1, 2, 3]
cloned_list = list(original_list)
# The above methods will not work if we have a list of objects (i.e., a list of lists). In this case, we need a DEEP COPY
# 4. Using copy.deepcopy() for deep copies
import copy

original_list = [[1, 2], [3, 4]]
cloned_list = copy.deepcopy(original_list)

# EXERCISE BEGINS BELOW
from typing import List


# takes a list of integers and returns a new list with the specified element removed. don't modify the original list
def remove_element(arr: List[int], element: int) -> List[int]:
    newArr = arr[:]
    newArr.remove(element)
    return newArr


# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
