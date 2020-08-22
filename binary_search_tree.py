"""
Binary Search Tree

A BST or Ordered/Sorted Binary Tree is a binary tree in which all the node
values to the left child of its parent are less and all the node values to the
right child of parent is more.

A perfect balanced binary search tree will have O(log n) for insert, remove and
search operations

Insert
	• if no node is present, the first element becomes the root
	• If a root element is present, the incoming element is checked to see if it's < or > root and moved to the left and right of the root accordingly. This is the same method if there are root and children already present
Delete
	• If it' s leaf node, simply remove it
	• if the node has only one child, link the child to the node's parent and remove the node
	• If the node to be removed has two children, then we find the smallest node in the right subtree and swap node to be removed with the smallest node and delete the node. If no right subtree is present, get the largest value in the left sub-tree (which is a direct left descendant) and swap it and delete the original node.

Traversing
	• Pre-Order - Root, Left, Right
	• In-Order - Left, Root, Right <--- gives a sorted list
    • PostOrder - Left, Right, Root
"""

class BST:
    def __init__(self, key = None):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self, level=0): # pre-order
        ret = "\t" * level + "Key: " + str(self.key) + "\n"
        if self.left:
            ret += self.left.__repr__(level+1)
        if self.right:
            ret += self.right.__repr__(level+1)
        return ret

def insert_key(root, key):
    # base case
    if not root:
        return BST(key)
    else:
        if key < root.key:
            root.left = insert_key(root.left, key)
        else:
            root.right = insert_key(root.right, key)

    return root

def delete_key(root, key):
    if root is None:
        return root
    
    if key < root.key:
        root.left = delete_key(root.left, key)
    elif key > root.key:
        root.right = delete_key(root.right, key)
    else: # node to be deleted

        # node has one or no children
        if root.left is None:
            temp = root.left
            root = None
            return temp
        elif root.right is None:
            temp = root.right
            root = None
            return temp

        # Node with two children, get in-order successor, which is the min value
        # in right subtree
        min_val_node = get_min_val(root.right)
        root.key = min_val_node.key
        root.right = delete_key(root.right, min_val_node.key)
        
    return root

def get_min_val(node):
    current = node  
    while(current.left is not None): 
        current = current.left  
  
    return current  

def traversal(root, type):
    if type == "inorder":
        if not root:
            return
        else:
            traversal(root.left, "inorder")
            print(root.key, end = " ")
            traversal(root.right, "inorder")
    elif type == "preorder":
        if not root:
            return
        else:
            print(root.key, end = " ")
            traversal(root.left, "preorder")            
            traversal(root.right, "preorder")
    elif type == "postorder":
        if not root:
            return
        else:            
            traversal(root.left, "postorder")            
            traversal(root.right, "postorder")
            print(root.key, end = " ")

root = insert_key(None, 50)
root = insert_key(root, 30) 
root = insert_key(root, 20) 
root = insert_key(root, 40) 
root = insert_key(root, 70) 
root = insert_key(root, 60) 
root = insert_key(root, 80)

print("\nIn-order traversal of BST")
traversal(root, "inorder")
print()

print("\nPreorder traversal of BST")
traversal(root, "preorder")
print()

print("\nPostorder traversal of BST")
traversal(root, "postorder")
print()


print("\nDelete 20")
root = delete_key(root, 20) 

print()
print(repr(root))