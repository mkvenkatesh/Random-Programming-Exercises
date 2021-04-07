# Implement a hash table using arrays

# 1. Create an array of size N
# 2. For a given key, computer hash(key) and take modulo or N to plug it into an
#    index in the array
# 3. The array will have references to a linked list that stores the key/values
#    for a key that maps to that index

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, node):
        temp = self.head
        self.head = node
        self.head.next = temp

    def remove(self, key):
        curr = self.head
        prev = self.head
        while curr != None:
            if curr.key == key:
                if curr == self.head:
                    self.head = curr.next
                else:
                    prev.next = curr.next
            prev = curr
            curr = curr.next

    def get_value(self, key):
        curr = self.head
        while curr != None:
            if curr.key == key:
                return curr.value
            curr = curr.next

    def get_node_for_key(self, key):
        curr = self.head
        while curr != None:
            if curr.key == key:
                return curr
            curr = curr.next

    def print(self):
        curr = self.head
        while curr != None:
            print(curr.key, curr.value)
            curr = curr.next

class HashTable:
    def __init__(self):
        self.hashtable = [None] * 10

    def get_key_index(self, key):
        key_hash = hash(str(key))
        if key_hash < 0:
            key_hash *= -1

        # Get index of array from hash
        key_index = key_hash % len(self.hashtable)
        return key_index

    def set(self, key, value):
        if key == None or len(str.strip(str(key))) == 0:
            print("ERROR: key is not provided.")
        
        # calculate the hash & index of the key        
        key_index = self.get_key_index(key)

        # if array index is null, create a linked list and start adding nodes
        if not self.hashtable[key_index]:
            self.hashtable[key_index] = LinkedList()

        # if a key already exist in the linked list, update it. If not add a new node
        l = self.hashtable[key_index]
        node_with_key = l.get_node_for_key(key)
        if node_with_key:
            node_with_key.value = value
        else:
            l.add(Node(key, value))

    def get(self, key):
        # calculate the hash & index of the key        
        key_index = self.get_key_index(key)

        # search for the key in the linked list in that array index
        return self.hashtable[key_index].get_value(key)

ht = HashTable()
ht.set('america', 900000)
ht.set('america', 10)
ht.set('africa', 1000)
ht.set('europe', 1000000)
ht.set('asia', 7000000)
ht.set('australia', 98009)
ht.set('arabia', 12023)
print()
print(ht.get("asia"))
print(ht.get("america"))
print(ht.get("europe"))