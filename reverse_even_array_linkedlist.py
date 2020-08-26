import math
# Add any extra import statements you may need here


class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here
def reverse_keys(left, even_array):
  # 1 -> 2 -> 8 -> 4 -> 9
  # L              
  idx = 0
  while (left and left.data % 2 == 0):
    left.data = even_array[idx]
    left = left.next
    idx += 1
  
  

def reverse(head):
  # Write your code here
  # walk the linked list. check if next node's key is even or odd
  # if it's even, store the current node in a start var.
  # if it's odd, go to the next node and check again
  # once an even is hit, don't overwrite the start var, keep on waking until you hit odd/end
  # do store even pointer as you walk the evens.
  # store start.next in a var, point start.next to last_even, and temp.next = last_even.next
  # walk
  
  left_ptr = None  
  current = head
  even_array = []
  while current:
    # if current key is even, store current in a left_ptr var as long it's the first occurrence of even
    if (current.data % 2 == 0):
      if not left_ptr:
        left_ptr = current
      # if left_ptr is already defined and we encounter even, store the current in right_ptr and walk
      even_array.append(current.data)
      right_ptr = current
      current = current.next
      continue
      
    # if current.next is odd and left_ptr is none, then we've only encountered head or odd's so far. keep walking.
    if (current.data % 2 != 0):
      if not left_ptr:
        current = current.next
      else:
        if len(even_array) > 1:
          reverse_keys(left_ptr, even_array[::-1])
        left_ptr = None
        even_array = []
        current = current.next
        
    # if we reach the end of the linked list and we still have valid left/right ptrs, swap them.    
  if left_ptr and len(even_array) > 1:
    reverse_keys(left_ptr, even_array[::-1])

  return head  
      










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printLinkedList(head):
  print('[', end='')
  while head != None:
    print(head.data, end='')
    head = head.next
    if head != None:
      print(' ', end='')
  print(']', end='')

test_case_number = 1

def check(expectedHead, outputHead):
  global test_case_number
  tempExpectedHead = expectedHead
  tempOutputHead = outputHead
  result = True
  while expectedHead != None and outputHead != None:
    result &= (expectedHead.data == outputHead.data)
    expectedHead = expectedHead.next
    outputHead = outputHead.next

  if not(outputHead == None and expectedHead == None):
    result = False

  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printLinkedList(tempExpectedHead)
    print(' Your output: ', end='')
    printLinkedList(tempOutputHead)
    print()
  test_case_number += 1

def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead

if __name__ == "__main__":
  head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
  expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
  output_1 = reverse(head_1)
  check(expected_1, output_1)

  head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
  expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
  output_2 = reverse(head_2)
  check(expected_2, output_2)

  # Add your own test cases here
  