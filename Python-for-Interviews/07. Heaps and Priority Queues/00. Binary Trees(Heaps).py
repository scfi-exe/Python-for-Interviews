import math

# https://www.youtube.com/watch?v=HqPJF2L5h9U
# binary tree mat his a bit easier to do if we consider i[0] to be "i = 1", so that we can do the below math:
# If a node is at index: i
# It's left child is at: 2*i
# It's right child is at: 2*i+1
# It's parent is at i//2 --> has to be floor division, i.e., if i=7 then it's parent is 3.5, but we want to get the value 3 and NOT round up to 4

# FULL vs COMPLETE binary tree
# all binary tree's have a height(depth), with the top parent element starting at height=0
# at each height, there is a maximum number of nodes. i.e., height0:maxNodes==1, height1:maxNodes==2, height2:maxNodes==4, height3:maxNodes==6

# if a TREE has the MAX # OF NODES for it's height, then that is a FULL TREE
# if the HEIGHT of a binary tree is 'h', then a tree can have maxNodes == ((2^(h+1))-1) nodes
# height of binary tree is log n

# if a TREE is MISSING ELEMENTS between the FIRST and LAST element, then that is an INCOMPLETE binary tree
# --> i.e., if represented in an array, there should be no gaps in between any of the elements/missing indices between the i[0] and i[-1]
# if a TREE has NO MISSING ELEMENTS between the FIRST and LAST element, then it is a COMPLETE binary tree

# EVERY FULL binary tree is ALSO A COMPLETE binary tree
# NOT every COMPLETE binary tree is a FULL binary tree


def print_binary_tree(arr):
    n = len(arr)
    levels = math.floor(math.log2(n)) + 1 if n > 0 else 0

    max_width = 2 ** (levels - 1)  # number of nodes on the last level
    index = 0

    for level in range(levels):
        # Number of nodes on this level
        count = 2**level
        # Spaces between nodes (rough formatting)
        spacing = max_width // count

        line = ""
        for i in range(count):
            if index < n:
                line += " " * spacing + str(arr[index]) + " " * spacing
                index += 1
        print(line.center(max_width * 4))  # scale spacing for readability


# Example usage:
arr = [10, 15, 20, 30, 40, 50, 60]
print_binary_tree(arr)
#      10          height: 0
#   15     20      height: 1
# 30  40  50 60    height: 2
