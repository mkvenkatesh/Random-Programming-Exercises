"""
Trie (pronounced "try") - a tree data structure that holds strings

Notes
* Every trie node has two elements. One if a hash table that maps the character
  to a trie node, this is used to establish a parent-child relationship and
  another is a boolean value to signify if the character that represents this
  node is end of word or not.

    TrieNode {
        map<character, TrieNode> children;
        boolean endOfWord;
    }

# Insertion - O(l * n), where l is the average length of the word and n is the
number of words
a. initially current node is root . Loop through the characters of the first
string.
b. For each character, check if it's in the hash table of the current node. If
it is, move to the child of it and increment character and repeat
c. If the character is not found in the current node, create a new node with F/T
boolean based of if it's the end of string or not and set the character as the
key and the new node as the value in the current node's map table and set the
current node to it's child. Increment character in string and repeat.

# Deletion - O(l*n)
As you move through each character in the word through the trie, if you reach
end of the word (true) and you exhaust your string, check if that node has any
hash values. If it does, simply turn the end of word to False on that node. If
the hash is empty, delete the node and go up one level. Delete the map value for
which we deleted its child and if the node is now empty and has a 'False' end of
word, delete this and repeat this.

# Search
Prefix Based - O(l)
It's pretty straightforward. You walk from the root and check if first character
exists or not and move to the children and check the next character. As soon as
you find the prefix, you know that there's at least one word with that prefix in
the trie. return true. If something doesn't exist, return false.

Whole String - O(l) to search the word where l is the length Same as prefix
based search but as you reach the end node and end of string, you check the see
if the end node in trie has end of word boolean set to 'True

print root hash table, end_of_word and queue the child nodes into an array and
loop through and print all the children until array is empty
"""

class TrieNode:
    def __init__(self, children = {}, end_of_word = False):
        self.children = children
        self.end_of_word = end_of_word

    def insert(self, word):
        current_node = self
        end_of_word = False
        for idx, letter in enumerate(word):
            if idx == len(word)-1:
                end_of_word = True

            # If the letter exist in the current node, move to the child pointed by
            # it. If the letter is end of the word, make the child node True.
            if letter in current_node.children:
                current_node = current_node.children[letter]
                if (end_of_word):
                    current_node.end_of_word = end_of_word
            # if the letter doesn't exist, create an empty node, insert the letter
            # into current node as key and value as the empty node. if endOfword,
            # set child node end_of_word to True.
            else:
                child_node = TrieNode({}, False)
                if (end_of_word):
                    child_node.end_of_word = end_of_word
                current_node.children[letter] = child_node
                current_node = child_node

        print(f"Word '{word}' is inserted into the trie.")

    def delete(self, word):
        seen_nodes = []
        current_node = self
        for letter in word:
            if letter in current_node.children:                
                # add the current node to the seen list so that it can be
                # reviewed later to see if it should be deleted
                seen_nodes.append((current_node, letter))
                current_node = current_node.children[letter]
            else:
                print(f"Deletion stopped. Word '{word}' does not exist.'")
                return

        # if we have traversed all the nodes until end of the string and if the
        # current node's end of word is set to False, then we haven't found the
        # word.
        if (not current_node.end_of_word):
            print(f"Deletion stopped. Word '{word}' does not exist.'")
            return

        if len(current_node.children) > 0 and current_node.end_of_word:
            current_node.end_of_word = False
            print(f"Word '{word}' deleted successfully from the trie.")
            return

        # Now trace back and delete empty nodes or map values in existing nodes
        current_letter = ""
        while True:
            # if empty node, remove it and trace back
            if current_node.children == {}:
                del current_node
                if seen_nodes == []:
                    print(f"Word '{word}' deleted successfully from the trie.")
                    return
                current_node = seen_nodes[-1][0]
                current_letter = seen_nodes[-1][1]
                del seen_nodes[-1]
            # if not empty node, clean up map values with invalid object
            # references and remove the node only if end of word is False and
            # map is empty
            else:
                # clean up the map for the invalid reference
                del current_node.children[current_letter]
                if (current_node.children == {} and current_node.end_of_word) or (current_node.children != {}):
                    print(f"Word '{word}' deleted successfully from the trie.")
                    return        

    def search(self, type, letters):
        current_node = self
        for letter in letters:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                print(f"'{letters}' is not found in the trie.")
                return
        
        if (not current_node.end_of_word) and type == "word":
            print(f"'{letters}' is not found in the trie.")
            return

        print(f"'{letters}' is found in the trie.")

    def __repr__(self, level=0):
        ret = "\t" * level + "Keys: " + "".join(self.children.keys()) + "; EndOfWord: " + str(self.end_of_word) + "\n"
        for child in self.children.values():
            ret += child.__repr__(level+1)
        return ret


# create root node
root = TrieNode()

s = ["abc", "abgl", "cdf", "abcd", "lmn"]

print()
# insert all the words into the trie - O(n*l)
for word in s:
    root.insert(word)

print()
print("\n************ Trie ************")
print(repr(root))

# Search prefixes in the trie - O(l)
root.search("prefix", "ab")
root.search("prefix", "bc")

print()
# Search words in the trie - O(l)
root.search("word", "abc")
root.search("word", "abcg")

print()

# delete words in the trie O(n*l)
s = ["abc", "abgl", "cdf", "abcd", "lmn"]
for word in s:
    root.delete(word)

print("\n************ Trie ************")
print(repr(root))