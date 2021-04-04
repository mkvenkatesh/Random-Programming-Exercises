# Reverse Array

class Solution:
    def __init__(self, arrtoreverse):
        self.arrtoreverse = arrtoreverse
    
    def reverse(self):
        for i in range(len(self.arrtoreverse)//2):
            swap_index = len(self.arrtoreverse) - i - 1
            self.arrtoreverse[i], self.arrtoreverse[swap_index] = self.arrtoreverse[swap_index], self.arrtoreverse[i]

arr = [1, 2, 3, 4, 5, 6]
s = Solution(arr)
s.reverse()
print(arr)