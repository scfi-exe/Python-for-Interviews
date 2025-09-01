# python has built in min() and max() functions to find the minimum values
# we can use these functions to condense the following code:
transactions = -2

if transactions < 0:
    transactions = 0
# into:
transactions = -2

transactions = max(0, transactions)

# we can also use the min() function to make sure a value doesn't exceed a certain limit
transactions = 101
# This will ensure transactions is never greater than 100
if transactions > 100:
    transactions = 100
# This is equivalent to the above code
transactions = min(100, transactions)

### challenge starts below ###
from typing import List


# takes an integer and returns the int if it is greater than or equal to 0, else: returns 0
def disallow_negatives(num: int) -> int:
    return max(0, num)


# takes a list of integers, and returns the max difference between any 2 ADJACENT integers in the list
def max_difference(nums: List[int]) -> int:
    differences = []
    for num in range(len(nums) - 1):
        differences.append(nums[num + 1] - nums[num])
    return max(differences)


# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
