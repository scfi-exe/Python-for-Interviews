# in algorithms, it's very common to count the frequency of elements in a list or a string.
# the most straightforward way to do this is with the following code:
nums = [1, 2, 3, 4, 5]
freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
# the above code iterate through nums. if a number is not already in the dict, it adds it with the value of 1
# if a number is already in the list, it increments the value (count) by a count of 1

# the collections module also provides a class called defaultdict that allows you to set values for keys that are not in the dict yet
# this is very useful when counting the frequency of elements in a list. consider the following code:
from collections import defaultdict

nums = [1, 2, 4, 3, 2, 1, 2]
freq = defaultdict(int)

for num in nums:
    freq[num] += 1
print(freq)
