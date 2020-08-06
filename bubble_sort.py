"""
Bubble Sorting

Worst case - O(N^2); Space - O(1)

# Algorithm

Bubble sort is one of the simplest sorting algorithms and really intuitive to
understand. We compare adjacent elements and see if their order is wrong (a[i] >
a[j] for 1 <= i < j <= size of array; if array is to be in ascending order, and
vice-versa). If yes, then swap them.

bubbleSort( Arr[], totat_elements)

   for i = 0 to total_elements - 1 do: swapped = false       
      for j = 0 to total_elements - i - 2 do:    
         /* compare the adjacent elements */   
         if Arr[j] > Arr[j+1] then /* swap them */ swap(Arr[j], Arr[j+1])       
            swapped = true end if         
      end for      
      /*if no number was swapped that means array is sorted now, break the
      loop.*/      
      if(not swapped) then break end if      
   end for   
end

# Example

[5, 4, 3, 2, 1, 29]

"""

def bubble_sort(array):    
    array_index_end = len(array) - 1
    done = True
    while done:
        done = False
        for i in range(0, array_index_end):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                done = True

        array_index_end -= 1

    return array

input_array = [5, 4, 4, 3, 2, 1, 29, 87, 66]
print(bubble_sort(input_array))