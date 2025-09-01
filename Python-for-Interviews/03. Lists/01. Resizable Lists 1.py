# some languages have both fixed-size arrays and resizable arrays. in python, we ONLY have resizable arrays, called LISTS
# this means that we can add elements to or remove elements from a list at any time
# common operations on a list include:
# 1. append() --> add an element to the end of the list
# 2. pop() --> removes and returns the last element of a list
#    if the list is already empty, we will get an IndexError
#    we can also pass an Integer to pop() to remove an element at a specific index in the list
#    if we pop(index) an index that is out of bounds, we will get an IndexError
# 3. insert() --> inserts an element as a specified index in a list
#    if the index is out of bounds, we will get an IndexError

# append() time complexity: O(1)
# pop() time complexity: O(1)
# insert() time complexity: O(n), where n is the number of elements in the list


from typing import List


# should append the elements of arr2 to the end of arr1 and return the resulting list
def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for item in arr2:
        arr1.append(item)
    return arr1


# should remove the last n elements from the list, and return the resulting list
# if n is greater than the length of the list, it shoudl return an empty list
def pop_n(arr: List[int], n: int) -> List[int]:
    if n > len(arr) - 1:
        return []
    else:
        for i in range(n):
            arr.pop()
    return arr


# insert the element at the specified index in the list and return the resulting list
# if index is out of bounds, you should insert it at the end of the list
def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    arr.insert(index, element)
    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
