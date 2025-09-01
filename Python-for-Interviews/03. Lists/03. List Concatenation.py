# instead of using extend() method, there is an even easier way to concatenate lists in Python: using the + operator
# the only difference between this and the extend() operator is that the + operator creates a NEW list, while extend() modifies the original list

from typing import List


# takes lists of two integers and returns a new list that contains all of the elements of the 1st list, followed by the 2nd list
# do NOT modify the original lists
def combine_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    return arr1 + arr2


# do not modify below this line
arr1 = [1, 3, 5]
arr2 = [4, 6, 8]

print(combine_elements(arr1, arr2))
print(arr1)
print(arr2)
