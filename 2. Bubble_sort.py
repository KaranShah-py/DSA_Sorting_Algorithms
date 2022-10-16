# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''

'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
Example: 
First Pass: 
( 5 1 4 2 8 ) -> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. 
( 1 5 4 2 8 ) ->  ( 1 4 5 2 8 ), Swap since 5 > 4 
( 1 4 5 2 8 ) ->  ( 1 4 2 5 8 ), Swap since 5 > 2 
( 1 4 2 5 8 ) -> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
Second Pass: 
( 1 4 2 5 8 ) -> ( 1 4 2 5 8 ) 
( 1 4 2 5 8 ) -> ( 1 2 4 5 8 ), Swap since 4 > 2 
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) ->  ( 1 2 4 5 8 ) 
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.
Third Pass: 
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) 
'''
# function
# Bubble sort to sort the list in ascending order
def bubble_sort_as(input_list, n):
    for i in range(n-1):
        swap = 0
        for j in range(0,n-1-i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swap = 1
        if swap == 0:
            break
    return input_list

# Bubble sort to sort the list in descending order
def bubble_sort_dsc(input_list, n):
    for i in range(n-1):
        swap = 0
        for j in range(0,n-1-i):
            if input_list[j] < input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swap = 1
        if swap == 0:
            break
    return input_list
            

# driver code
arr1 = [5,-4,344,1,11,10]      # Worst case
arr2 = [1,2,3,4,5]             # Best Case
print(arr1)
bubble_sort_as(arr1, len(arr1))
print(arr1)
bubble_sort_dsc(arr1, len(arr1))
print(arr1)

'''
Sorting algorithm          Best Case          Average Case         Worst Case          space          stable
Bubble Sort	                  O(n)	               O(n2)	           O(n2)            O(1)            Yes
'''

# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''