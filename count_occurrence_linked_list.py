"""
Question: Given a linked list of elements, count the number of occurrences of a given element

# Listen
# Questions
# Example
# BruteForce/Optimize/State the algorithm and ask if you can proceed with coding
# Code
# walkthrough the code
# Test the code with multiple test cases

# Example

n -> 1 -> 3 -> 3 -> 5 -> 2 -> null

Given a key k = 3, count the occurrences of 3 in the linked list.
So the answer above will be 2.

# Questions
1. Can I assume that this linked list will end in null?
2. Is it a single linked list?

"""

class LinkedList(object):
    def __init__(self, v, next = None):
        self.val = v
        self.next = next

l1 = LinkedList(1)
l2 = LinkedList(3)
l1.next = l2
l3 = LinkedList(3)
l2.next = l3
l4 = LinkedList(5)
l3.next = l4
l5 = LinkedList(2)
l4.next = l5

node = l1
linked_list_print = "Ptr -> "
while node.next != None:
    linked_list_print += str(node.val) + " -> "
    node = node.next

linked_list_print += "None"
print(linked_list_print)

# O(N) where N is the number of elements in the linked list and O(1) for space
def key_occurrence(node, key):
    occurrence = 0

    while node.next != None:
        if node.val == key:
            occurrence += 1
        
        node = node.next
    
    return occurrence

print(key_occurrence(l1, 3))
