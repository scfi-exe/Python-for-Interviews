# we can also use UNPACKING in LOOPS to iterate over a list of lists
# this is useful WHEN we know the size of the inner lists, and want to unpack them into variables
# points = [[0, 0], [2, 4], [5, 8], [2, 3]]
# for x, y in points:
#     print(f"X: {x}, Y: {y}")

from typing import List, Tuple


# takes a list of tuples (name, score). find the student with the highest SCORE and return their name
def best_student(scores: List[Tuple[str, int]]) -> str:
    highScore = 0
    highScoreHolder = "none"
    for name, score in scores:
        if score > highScore:
            highScore = score
            highScoreHolder = name
    return highScoreHolder
    pass


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
