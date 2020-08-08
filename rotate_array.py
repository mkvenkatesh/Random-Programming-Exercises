class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        for i in range(len(a)):
            ret.append(a[(i + b) % len(a)])
        return ret

s = Solution()

print(s.rotateArray([1, 2, 3, 4, 5], 2))