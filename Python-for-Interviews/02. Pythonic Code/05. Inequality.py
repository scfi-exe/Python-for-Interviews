# Python allows us to make small shortcuts when making multiple comparisons
# i.e., "if 0 < X and X < 10:" is equivalent to "if 0 < X < 10:" in Python
from typing import List


# should return True if the length of the list of names is greater than 0 AND <= the parameter maxLength
# otherwise, should return False
def is_arr_valid(names: List[str], max_length: int) -> bool:
    if 0 < len(names) <= max_length:
        return True
    else:
        return False


# do not modify below this line
print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 1))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 4))
