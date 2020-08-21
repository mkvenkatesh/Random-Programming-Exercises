"""
Linked List

"""

class LinkedList:
    def __init__(self, data_array=None):
        self.head = None
        if data_array is not None:
            node = Node(data_array.pop(0))
            self.head = node
            for data in data_array:
                node.next = Node(data)
                node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self: # self is iterable because of the __iter__ defined below.
            pass
        current_node.next = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        current = self.head
        nodes = []
        while current != None:
            nodes.append(str(current.data))
            current = current.next
        nodes.append("Tail")
        return " -> ".join(nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList()

node1 = Node(10)
llist.head = node1

print(repr(llist))

node2 = Node(250)
node1.next = node2

print(repr(llist))

# using a data array

llist = LinkedList([10, 20, 30, 40, 50])

llist.add_first(Node(5))
llist.add_last(Node(55))

print(repr(llist))

# using __iter__ to create an iterable definition in the class and use it as a
# generator below
for node in llist:
    print(node.data)