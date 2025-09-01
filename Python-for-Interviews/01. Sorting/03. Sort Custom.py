from typing import List

# we can do a custom sort using the "key" parameter in the sort() method
# the "key" parameter doesn't accept a value. instead, it accepts a function that returns a value to be used for sorting


def getWordLength(word):
    return len(word)


# accepts a list of words and sorts them by their length, in descending order
def sort_words(words: List[str]) -> List[str]:
    words.sort(key=getWordLength, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=abs)
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
