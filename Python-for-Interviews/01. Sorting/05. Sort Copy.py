# there is another way to sort in Python
# unlike .sort(), the sorted() function returns a NEW list with elements in the sorted order, leaving the original list unchanged
# the sorted() fxn works similar to the .sort() fxn, in that you can still do things like sorted(list, key= lambda word: len(word), reverse=True)

from typing import List


# accepts a list of words and returns a NEW list of words, sorted in ASCENDING order --> do NOT modify the original list
def sort_words(words: List[str]) -> List[str]:
    sortedWords = sorted(words)
    return sortedWords


# accepts a list of numbers and returns a NEW list of numbers, sorted in DESCENDING order based on ABSolute value -> dont mod OG list
def sort_numbers(numbers: List[int]) -> List[int]:
    sortedNumbers = sorted(numbers, key=lambda num: abs(num), reverse=True)
    return sortedNumbers


# do not modify below this line
original_words = [
    "cherry",
    "apple",
    "blueberry",
    "banana",
    "watermelon",
    "zucchini",
    "kiwi",
    "pear",
]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))
