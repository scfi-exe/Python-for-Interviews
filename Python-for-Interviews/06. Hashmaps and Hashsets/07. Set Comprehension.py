# just like with Lists and Dictionaries, Python also supports SET COMPREHENSION
# nums = [1, 3, 5]
# squared = {num * num for num in nums}
# print(squared)
# in the above code, we created a set where the elements are the square of each number in the list nums
# notice that the syntax is similar to LIST COMPREHENSION, but we use CURLY BRACKETS instead of square brackets

# both Dictionaries and Sets use curly brackets
# the difference is that Dictionaries have key:value pairs separated by a colon in the brackets, whereas Sets only have the elements themselves.

from typing import List, Set


# write a function that sets a list of integers and converts it into a set of integers with the double of each number in the list
def double_nums(numss: List[int]) -> Set[int]:
    doubled = {num * 2 for num in numss}
    return doubled


# do not modify below this line

output1 = double_nums([1, 2, 3])
print(type(output1))
print(sorted(list(output1)))

output2 = double_nums([4, -2, 0, 7])
print(type(output2))
print(sorted(list(output2)))

output3 = double_nums([10, 20, 30, 40, 50])
print(type(output3))
print(sorted(list(output3)))
