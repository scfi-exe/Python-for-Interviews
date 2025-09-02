# behind lists, hash maps are the most commonly-used data structure in Python
# a HASH MAP is a collection of key-value pairs
# each key is UNIQUE, and it maps to a specific value. keys may be of any immutable type (integers, strings, tuples)

# hash maps are implemented using the DICTIONARY class. common operations in a hash map include:
# 1. INSERTION: insert a key:value pair into the hash map
my_dict = {}
my_dict["a"] = 1  # {'a': 1}
# 2. ACCESS: access the value associated with a key
my_dict = {"a": 1}
# print(my_dict['a']) #1
# 3. DELETION: delelte a key-value pair from the hash map
my_dict = {"a": 1, "b": 2}
del my_dict["a"]  # return None
my_dict.pop("b")  # return 2
# my_dict.pop('c') # KeyError: 'c' (not found)
# my_dict.pip('c', 'default') #No error, returns "default"

# 4. LOOKUP: Check if a key exists in a hash map
my_dict = {"a": 1}
does_a_exist = "a" in my_dict  # True
does_b_exist = "b" in my_dict  # False
# for lookup operations, you can also use the IN operator, similar to how you would lookup lists


from typing import List, Dict


# takes two lists, keys and values, and returns a hash map where the keys are elements of the keys list and values are elements of the values lies
def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    hashMap = {}
    for element in range(len(keys)):
        hashMap[keys[element]] = values[element]
    return hashMap


def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    values = []
    for element in range(len(keys)):
        # return hash_map[element]
        print(hash_map[keys[element]])


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(
    get_values(
        {
            "Jane": 25,
            "Charlie": 60,
            "Carol": 100,
        },
        ["Jane", "Carol"],
    )
)
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
