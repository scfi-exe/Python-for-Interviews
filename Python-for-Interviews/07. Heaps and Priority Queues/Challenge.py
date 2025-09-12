# Input:
# nums = [3,4,5,6], target = 7
#
# Output: [0,1]
#


def twoSum(list, target):
    for num1 in range(len(list)):
        for num2 in range(
            num1 + 1, len(list)
        ):  # be sure to do num1+1, otherwise you will output duplicates
            if list[num1] + list[num2] == target:
                return [num1, num2]
            else:
                pass


print(twoSum([3, 4, 5, 7], 7))
