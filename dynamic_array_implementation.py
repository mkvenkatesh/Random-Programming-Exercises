# Implement dynamic arrays, similar to Java's ArrayList. By default, python
# lists are dynamic arrays, so just try to simulate static arrays in python

class DynamicArray:
    
    CAPACITY_INC_SIZE = 2
    
    def __init__(self, size):
        self.dynamic_array = [None] * size
        self.index = 0

    def append(self, item):
        if self.dynamic_array[-1] != None:
            self.inc_size_and_copy_array()

        self.dynamic_array[self.index] = item
        self.index += 1

    def get(self, index):
        if index <= self.index - 1:
            return self.dynamic_array[index]
        else:
            return 'Error: index doesn''t exist'

    def len(self):
        return self.index

    def size(self):
        return len(self.dynamic_array)

    def inc_size_and_copy_array(self):
        temp = [None] * (len(self.dynamic_array) * self.CAPACITY_INC_SIZE)
        for idx, item in enumerate(self.dynamic_array):
            temp[idx] = item
        self.dynamic_array = temp        

    def __str__(self):
        return " ".join(str(self.dynamic_array[:self.index]))

da = DynamicArray(2)
da.append(10)
da.append(20)
da.append(30)
print(da)
print('Array Length: ', da.len())
print('Array Size:', da.size())
da.append(40)
da.append(50)
print('Array Length: ', da.len())
print('Array Size: ', da.size())
print(da)
print(da.get(0))
print(da.get(9))
print(da.get(4))