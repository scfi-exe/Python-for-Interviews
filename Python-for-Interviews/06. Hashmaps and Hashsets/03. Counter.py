# if ALL we want to do is count the number of occurences of each element in a list, an even better solution exists
# we can use the collections.Counter class, which is a subset of the Dict class
# Counter returns a Dictionary where the KEYS are the elements in a list, and the VALUES are the occurences of each element
# It behaves similarly to a defaultdict with an integer default value, meaning that if a key doesn't exist, it will return 0

# Tip: if we want to count the number of occurences of multiple lists or strings, we can use the update() method:
# nums1 = [1, 2, 3, 4]
# nums2 = [5, 6, 7, 8]
# from collections import Counter

# counter = Counter(nums1)
# counter.update(nums2)
# print(counter)

from collections import Counter
from typing import Counter as CounterType


# create a fxn that takes two strings and returns a Counter object that counts the occurences of each element in each string
def count_chars(s1: str, s2: str) -> CounterType:
    output = Counter(s1)
    Counter.update(s2)
    return output


# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
