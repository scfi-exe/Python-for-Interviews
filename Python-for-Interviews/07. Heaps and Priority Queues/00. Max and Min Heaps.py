# condition 1: a HEAP is a COMPLETE binary tree
# condition 2, max: in a MAX heap, every PARENT has a GREATER VALUE than (or equal value to) it's DESCENDANTS
# condition 2, min: in a MIN heap, every PARENT has a LOWER VALUE than it's DESCENDANTS
import heapq

# INSERT OPERATION in a MAX HEAP
maxHeap = [
    50,
    30,
    20,
    15,
    10,
    8,
    16,
]  # i want to insert 60, and the root should have the largest element, so 60 should push to the root i=0
heapq.heapify(maxHeap, reverse=True)
print(maxHeap)
