# Python provides an easy way to iterate over multiple lists at a time, using the .zip() function
# zip() takes multiple lists as inputs and returns an interator of tuples
# each tuple contains an element from each list
# this is helpful when we have multiple lists of the SAME LENGTH and we want to iterate over them together

# names = ["Alice", "Bob", "Charlie", "Kyra"]
# scores = [90, 85, 88, 92]
# for name, score in zip(names, scores):
#     print(f"{name} scored {score}%")

from typing import List, Dict


# takes two lists, 'name' and 'scores', and returns a dict where key is names[i] and it maps to scores[i] as the value
def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    newDict = {}
    for name, score in zip(names, scores):
        newDict[name] = score
    return newDict


# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
