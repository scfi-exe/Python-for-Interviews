# similar to list comprehension, python also supports dictionary comprehension
# we can use dict comprehension to initialize dictionaries in a more concise way
# nums = [1, 2, 3, 4]
# squared = {num: num * num for num in nums}
# print(squared)
#

from typing import List, Dict


# takes a list of integers and returns a dict where the keys are elements of the list and the values are indices of those elements in the list
def num_to_index(nums: List[int]) -> Dict[int, int]:
    return {nums[i]: i for i in range(len(nums))}


# do not modify below this line
print(num_to_index([1, 2, 3, 4, 5, 6, 7, 8]))
print(num_to_index([8, 7, 6, 5, 4, 3, 2, 1]))
print(num_to_index([0, 3, 2, 4, 5, 1]))
