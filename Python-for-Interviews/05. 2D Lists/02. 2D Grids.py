# it is common for a grid to be represented as a list of lists in python
# for example, a 2x3 grid can be represented as:
grid = [[0, 0, 0], [0, 0, 0]]

rows = len(grid)  # 2
cols = len(grid[0])  # 3

from typing import List

# in the above example, the variable "grid" is a list of lists. the variable "rows" is the # of rows in the grid
# and the variable "cols" is the number of columns in the grid
# WE ASSUME THAT EACH SUBLIST IN THE GRID HAS THE SAME LENGTH

# my solution, which was suboptimal
# def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
#     if r >= 0 and c >= 0:
#         if r <= len(grid) and c <= len(grid[0]):
#             return True
#         else:
#             return False
#     else:
#         return False


# optimized code / ideal solution
# takes a 2d grid of integers r and c, where r is the index of a row and c is the index of a column
# returns True if the cell atrow r and column c is within bounds of the grid, and False otherwies
def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    if 0 <= r <= len(grid) and 0 <= c <= len(grid[0]):
        return True
    else:
        return False


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
