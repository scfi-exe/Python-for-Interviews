# A very powerful feature in Python is COMPREHENSION. It allows us to create lists (and other data types) in a concise way.
# Here is an example:
# my_list = [i for i in range(5)]
# print(my_list)  # [0, 1, 2, 3, 4]
# above we have a for loop. BEFORE the for loop, we place the expression i, which is the value we want to add to the list

# comprehension is very flexible. below, we use zip() to iterate over 2 lists at a time, and pass i+j as the value to append
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
result = [i + j for i, j in zip(arr1, arr2)]

# we can also add a condition to the comprehension, like in the example below:
arr = [1, 2, 3, 4, 5]
result = [i for i in arr if i % 2 == 0]


# exercise starts below
from typing import List


# takes an integer and returns a list of all odd numbers from 1 to n, inclusive
def create_list_of_odds(n: int) -> List[int]:
    oddNumbers = [i for i in range(0, n + 1) if i % 2 != 0]
    return oddNumbers


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
