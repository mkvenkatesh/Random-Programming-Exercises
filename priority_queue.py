"""
Priority Queue

Priority Queue is an abstract data structure where the element with highest
priority (or lowest priority) is in front of the queue to be readily consumed.
It should support insertion and removal of elements into the queue as well.

Priority queues are best implemented with max/min heap data structure since it
provides O(1) for peek, and O(log n) for insert and delete operations for the
queue. 

Instead of implementing max/min heap from scratch, using python's built in heap
data structure
"""

import heapq

arr = [3, 4, 9, 5, 2, 1, 3, 10]

# by default, heapq does min-heap in python so we need to multiple everything by
# -1 to do max-heap
arr = [-x for x in arr] 

heapq.heapify(arr)
heapq.heappush(arr, -1 * 45)

print(f"\nmax-heap array: ", end="")
for i in arr:
    print(-1 * i, end=" ")
print()

# get first priority element
print()
elem = heapq.heappop(arr)
print(f"First Priority: {elem * -1}")

print(f"\nmax-heap array: ", end="")
for i in arr:
    print(-1 * i, end=" ")
print()