# in order to understand hash sets (and why they are different from lists), we must first understand  indexing vs searching
# INDEXING is when we jump to a point in a dataset, i.e., list[3] -> indexing is FAST for lists, O(1), and nonexistent for sets
# since you can't index sets, you can't say mySet[2]
# SEARCHING is when you are looking through an entire dataset for a specific value or values
# Searching is very SLOW, O(n), in LISTS because Python has to scan each element in the list until it finds the value in question
# Searching is very FAST, O(1) on average, because it hashes X and only checks that slot
# It's very likely that most things you've interacted with online are hash sets, not lists. for example:
# --> characters on a video game server, ebay auction listings, a Facebook friends list, google search data, youtube videos, etc
# although many frontend UIs use a list view, many backend UIs likely use hash sets to store (or at least search through) data

# Common Operations on a Hash Set include:
# 1. Insertion [mySet.add(x)]: Insert a key into the hash set
# my_set = set()
# my_set.add('a') # {'a'}

# 2. Deletion [mySet.remove(x) and mySet.discard(x)]: Delete a key from the hash set
# The mySet.remove() method will remove an element from a list. If the element does not exist in the list, the method will raise a KeyError
# The mySet.discard() method will remove an element from a list, and will NOT raise a KeyError if the value oes not exist.
# my_set = {'a'}
# my_set.remove('a') # {}
# my_set.remove('a') # KeyError
# my_set.add('b')
# my_set.discard('b') # {}
# my_set.discard('b') # No Error

# 3. Lookup [x in mySet]: Check if a key exists in the hash set
# my_set = {'a'}
# 'a' in my_set #True
# 'b' in my_set #False

# TIME COMPLEXITY --> Insertion O(1) // Deletion O(1) // Lookup O(1)

### BEGIN EXERCISE ###

from typing import List, Set


# takes a list of strings -> returns a hash set containing those strings
def build_hash_set(keys: List[str]) -> Set[str]:
    pass


# takes a hash set and a list of keys --> returns a list of booleans indicating whether each key exists in the hash set
# the order of booleans in the output list should match the order of keys in the input list
def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    pass


# do not modify below this line

output1 = build_hash_set(["Alice", "Bob", "Charlie"])
print(type(output1))  # check the type of the output
print(sorted(list(output1)))  # set order is not guaranteed so we need to sort the list

output2 = build_hash_set(["XY", "XX", "YY", "XY", "YX"])
print(type(output2))  # check the type of the output
print(sorted(list(output2)))  # set order is not guaranteed so we need to sort the list

print(check_keys({"Alice", "Bob", "Charlie"}, ["Alice", "Bob", "Charlie", "David"]))
print(check_keys({"a", "b", "c"}, ["a", "d", "c"]))
print(check_keys({"a", "c"}, ["d", "c"]))
