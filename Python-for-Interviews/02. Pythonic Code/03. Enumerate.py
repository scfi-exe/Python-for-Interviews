# suppose we wanted to loop over an array and we want to access both the index AND the element at that index
# there are other ways to accomplish this, but the most PYTHONIC way is using ENUMERATE function
# the main benefit of this approach is the readability improvement - it allows us to write self-documenting code

from typing import List


# returns the INDEX of the first occurence of the number 7 in the list 'nums'
# or, returns the index of the first occurence of -1, if the number 7 is not found
def get_index_of_seven(nums: List[int]) -> int:
    sevenFound = False
    for i, num in enumerate(nums):
        if num == 7:
            sevenFound = True
            return i
    if sevenFound == False:
        return -1


# returns the distance between the first and second occurence of the number 7 in the list nums
# you may assume that there will always be at least 2 occurences of the number 7
def get_dist_between_sevens(nums: List[int]) -> int:
    occurence1 = -225
    occurence2 = -225
    for i, num in enumerate(nums):
        if num == 7 and occurence1 == -225:
            occurence1 = i
        elif num == 7 and occurence2 == -225:
            occurence2 = i
    distanceBetween = occurence2 - occurence1
    return distanceBetween


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
