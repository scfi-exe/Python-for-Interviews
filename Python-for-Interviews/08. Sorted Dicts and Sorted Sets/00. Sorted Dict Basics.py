# python does not have built-in sorted dictionaries
# however, we can use the SORTED CONTAINERS library to create a sort dict in Python
# it suppors the same operations as a regular dictionary, but the keys are always sorted
# a sorted dictionary may NOT contain duplicate keys

# INSERTION: insert a key-value pair into the dict
from sortedcontainers import SortedDict

sorted_dict = SortedDict()
sorted_dict["A"] = 90
sorted_dict["B"] = 80
sorted_dict["C"] = 70
print(sorted_dict)  # SortedDict({'A': 90, 'B': 80, 'C': 70})

# ACCESS: Access the value associated with a key
sorted_dict = SortedDict({"a": 1})
print(sorted_dict["a"])  # 1

# DELETION: Delete a key-value pair form the sorted dicdt
sorted_dict = SortedDict({"a": 1, "b": 2, "c": 3, "d": 4})
# dict.popitem() removes & returns the last key-value pair in the sorted order
sorted_dict.popitem()  # ('d',1)

# dict.popitem(0) removes & returns the first key-value pair in soted order
sorted_dict.popitem(0)  # ('a',1)

# dict.pop(key) removes & returns the value associated with the key
sorted_dict.pop("b")  # 2

# del dict.[key] deletes the value and returns nothing, afaik
del sorted_dict["c"]  # {}

# LOOKUP: Check if a key exists in a sorted dict
sorted_dict = SortedDict({"a": 1})
does_a_exist = "a" in sorted_dict  # True
does_b_exist = "b" in sorted_dict  # False

# ITERATING: Loop through the sorted dict
sorted_dict = SortedDict({"a": 1, "b": 2, "c": 3})

for key, value in sorted_dict.items():
    print(key, value)
# Notice that we loop through the sorted dictionary using the items() method, which returns a list of key-value pairs.
# We will iterate over the key-value pairs in sorted order based on the keys. If we only iterated over the keys, but we
# needed the values as well, we would have to do a lookup for each key, which would be less efficient.
