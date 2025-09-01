# these List Operations are less-common, but absolutely still worth knowing
# 1. index() --> Returns the index of the first occurence of a specified element in a list
# 2. remove() --> Removes the first occurence of a specified element from a list
# 3. extend() --> Adds the elements of another list to the end of a list
# my_list = [1, 3, 2, 3]
# my_list.index(3) # Result: 1
# my_list.remove(3) # Result: [1, 2, 3]
# my_list.extend([4, 5]) # Result: [1, 2, 3, 4, 5]

# If we want to check if an element is in a list, we can use the "in" operator
# This is preferable to using index() unless we actually need the index of the element
# my_list = [1, 2, 3]

# if 3 in my_list:
#     print("3 is in the list")

# START CHALLENGE BELOW
from typing import List


# should append the elements of arr2 to the end of arr1 and return the resulting list
def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for item in arr2:
        arr1.append(item)
    return arr1


# should remove all elements of arr2 from arr1, and return the resulting list
def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for item in arr2:
        if item in arr1:
            arr1.remove(item)
    return arr1


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
