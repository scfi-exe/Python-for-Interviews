# # in algorithms, it's very common to count the frequency of elements in a list or a string.
# # the most straightforward way to do this is with the following code:
# nums = [1, 2, 3, 4, 5]
# freq = {}

# for num in nums:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# # print(freq)
# # the above code iterates through nums. if a number is not already in the dict, it adds it with the value of 1
# # if a number is already in the list, it increments the value (count) by a count of 1

# # the collections module also provides a class called defaultdict that allows you to set values for keys that are not in the dict yet
# # this is very useful when counting the frequency of elements in a list. consider the following code:
# # from collections import defaultdict
# nums = [1, 2, 4, 3, 2, 1, 2]
# freq = defaultdict(int)

# for num in nums:
#     freq[num] += 1
# # print(freq)

# # this pattern is also used with other data types, such as lists and sets
# # for example, if you want to create a dictionary where the default value is an empty list, you would use:
# nums = [1, 2, 4, 3, 2, 1]
# d = defaultdict(list)

# for num in nums:
#     d[num].append(num)

# print(d)  # {1: [1, 1], 2: [2, 2], 4: [4], 3: [3]}
# this will create a dictionary where each key is a number in the list, and the value is the list of all occurences of that number
# even if the number doesn't exist in the given dictionary, it will 1st create an empty value and then append the given num value to the list

### BEGIN EXERCISE###
#
#
from collections import defaultdict
from typing import List, Dict


# takes a string and returns the count of each letter in the string
def count_chars(s: str) -> Dict[str, int]:
    d = defaultdict(int)
    for char in s:
        d[char] += 1
    return d


# takes a list of list of integers and returns a dictionary where the keys are the first value of each list,
# and values are the remaining elements of each list
def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    output = defaultdict(list)

    for sublist in nums:
        first = sublist[0]
        # run a loop once for every value between 1 and len(sublist), append output[first] with sublist[i] on each loop
        for i in range(1, len(sublist)):
            output[first].append(sublist[i])
    return output


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
