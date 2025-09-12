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
