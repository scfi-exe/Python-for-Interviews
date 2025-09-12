# Sorted Sets are similar to Hash Seta, but they store keys in a sorted order
# Sorted sets may not contain duplicate elements
# The common operations on a sorted set include:

# INSERTION: Insert a key into the sorted set

from sortedcontainers import SortedSet

my_set = SortedSet()

my_set.add(90)
my_set.add(80)
my_set.add(70)
print(my_set)  # SortedSet([70, 80, 90])


# DELETION: Delete a key from the sorted set

my_set = SortedSet([90, 80, 85, 95])

my_set.remove(90)  # SortedSet([80, 85, 95])

my_set.discard(100)  # SortedSet([80, 85, 95])

my_set.pop()  # 95

my_set.pop(0)  # 80

print(my_set)  # SortedSet([85])

my_set.clear()  # SortedSet([])

# the set.remove(key) method will raise a KeyError if the element does not exist, while the set.discard(key) method will not
# the set.pop() method will remove and return the largest element in the sorted set
# the set.pop(0) method will remove and return the smallest element in the sorted set
# the set.clear() method will remove all elements from the sorted set


# LOOKUP: Check if a key exists in the sorted set
my_set = SortedSet([80, 85, 90])

does_a_exist = "a" in my_set  # True
does_b_exist = "b" in my_set  # False


# ITERATING: Loop through a sorted set

sorted_set = SortedSet([4, 3, 5, 2, 1])

for num in sorted_set:
    print(num)  # 1, 2, 3, 4, 5
