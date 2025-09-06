# it's common to store pairs of values in a dictionary or set
# for example, we might store the ROW,COLUMN pair of a cell in a grid
# while we cannot store the list as a key in a dictionary, we can use a TUPLE instead
dictOfPairs = {}

dictOfPairs[(0, 0)] = 1
dictOfPairs[(0, 1)] = 2

print(dictOfPairs)  # {(0,0):1, (0,1):2}

setOfPairs = set()
setOfPairs.add((0, 0))
setOfPairs.add((0, 1))
print(setOfPairs)  # {(0,0), (0,1)}
# in the above code, we created a DICT and a SET where the keys and elements are tuples
# we can use tuples to store pairs of values in a single object
# this is useful when we want to store multiple values together, but we don't want to create a new class or structure

# CHALLENGE

from typing import List, Set, Tuple


# takes a 2D grid of integers and returns a set of tuples where each tuple is a pair of the ROW and COLUMN
# The set should only contain the coordinates of cells that have a value of 1
def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    output = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                output.add((r, c))
    return output  # practice this, it was tough for me


# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))

output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
