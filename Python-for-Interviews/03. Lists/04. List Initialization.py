# If we want to create an empty list of a specific size, this is the way to do it in Python:
my_list = [0] * 5
# This is the standard way to create a list of a specific size in Python
my_list = [1] * 3
# The above code will create a list of three 1's

from typing import List


# should create and return a list of 'size'
# all values should be zero, except the the value at index[value], which should be equal to value
def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    myList = [0] * size
    myList[index] = value
    return myList


# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
