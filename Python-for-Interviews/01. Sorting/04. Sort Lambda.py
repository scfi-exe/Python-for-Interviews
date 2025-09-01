from typing import List

# having to define a function just to use it in a key can be annoying
# in these cases, lambda functions are helpful


# accepts a list of words and returns a new list of words sorted based on their length in DESCENDING order. use a lambda fxn
def sort_words(words: List[str]) -> List[str]:
    words.sort(key=lambda word: len(word), reverse=True)
    return words


# accepts a list of numbers and returns a new list of numbers based on their absolute value, in ascending order
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=lambda number: abs(number), reverse=False)
    return numbers


# do not modify below this line
print(
    sort_words(
        [
            "cherry",
            "apple",
            "blueberry",
            "banana",
            "watermelon",
            "zucchini",
            "kiwi",
            "pear",
        ]
    )
)

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
