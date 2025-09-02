# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for num in nums:
#             counter = count(nums(num)) > 2
#             print(counter)


def hasDuplicate(nums):
    twoCount = False
    numList = []
    for num in nums:
        numList.append(num)

    for num in numList:
        if numList.count(num) >= 2:
            twoCount = True

    if twoCount == True:
        print("True twoCount")
        return True
    else:
        print("False twoCount")
        return False


hasDuplicate([1, 2, 3, 3])
hasDuplicate([1, 2, 3])
