"""
Queue

Make sure to use the deque method from collections class for queue operations.
Using an array with array.pop(0) is a O(n) operation

You can also use Queue class but as a data structure it's cimply unnecessary.
deque() is good enough
"""

from collections import deque

queue = deque() # O(1)

# insert new element into the queue - O(1)
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# Pop the first element - # O(1)
queue.popleft() 

print(queue)


# You can provide any iterable to your deque function

queue = deque("intercodes") # O(1)
print(queue)

queue = deque([1, 2, 3, 4, 5])
print(queue)