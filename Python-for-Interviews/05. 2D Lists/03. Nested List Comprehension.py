# the optimal/standard way to initiate a grid is through nested list comprehension
grid = [[0 for i in range(3)] for j in range(2)]

grid[0][0] = 1

# print(grid)  # [[1, 0, 0], [0, 0, 0]]

# there is another, more precise version you may prefer that is equivalent to but more concise than the previous code
grid = [[0] * 3 for _ in range(2)]
# since the variable in the loop is not used, we use _ to indicate a throwaway (this is common python syntax)


from typing import List


def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    grid = [[value] * cols for _ in range(rows)]
    return grid


# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
