# a nested list is a list that contains other lists; a list of lists
# nestedList = [[1,2,3],[4,5,6],[7,8,9]]
# if we want to access elements in a nested lists, we can do so by chaining the indices: nestedList[0][1], nestedList [1,2]
# the lists do not need to all be the same length

from typing import List


# takes a 2D list of integers and returns a list of the maximum element from each sublist
# returned list should contain a max value from each sublist in the order they appear in the input list
def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    maxValues = []
    for arr in nested_arr:
        maxValue = 0
        for num in arr:
            maxValue = max(maxValue, num)
        maxValues.append(maxValue)

    return maxValues


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
