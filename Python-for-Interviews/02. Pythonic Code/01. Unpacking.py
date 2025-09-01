from typing import List, Tuple

# the biggest advantage of using Python in interviews is it's simplicity to read and write
# there are many shortcuts to improve readability, one of which is UNPACKING
point1 = [2, 4]
x1, y1 = (
    point1  # now x1 = 2 and y1 = 4 --> if the leftside of the equation is larger than the list, then VALUEERROR
)


# takes a list of 3 integers and returns the sum
def sum_3_integers(triplet: List[int]) -> int:
    x, y, z = triplet
    return sum(triplet)


# takes a list of 3 ints [width, height, depth] and returns the volume of it
def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    length, width, height = box_dimensions
    return length * width * height


# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
