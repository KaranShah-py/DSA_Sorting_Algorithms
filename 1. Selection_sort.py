# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''

'''
Selection Sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted. 
2) Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 

Following example explains the above steps:
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 
'''
# functions for ascending sorting
def select_sort_ascending(arr, n):
    for i in range(n-1):     
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j         
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Another way of coding for sorting ascendingly with the same logic used above 
def selection_sort_as(unsorted_list, n):
    for i in range(0, n-1):
        min_item_in = min(unsorted_list[i:])
        index_of_min = unsorted_list.index(min_item_in)
        unsorted_list[i], unsorted_list[index_of_min] = unsorted_list[index_of_min], unsorted_list[i]
    print(unsorted_list)

# Sorting descendingly 
def select_sort_descending(arr, n):
    for i in range(n-1):     
        max_idx = i
        for j in range(i+1, n):
            if arr[max_idx] < arr[j]:
                max_idx = j         
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

# Another method of code with the same logic 
def selection_sort_de(unsorted_list, n):
    for i in range(0, n-1):
        max_item_in = max(unsorted_list[i:])
        index_of_max = unsorted_list.index(max_item_in)
        unsorted_list[i], unsorted_list[index_of_max] = unsorted_list[index_of_max], unsorted_list[i]
    print(unsorted_list)



# driver code
arr = [5, 2, 6, 1, 3, 2]
selection_sort_as(arr, len(arr))
print(arr)


'''
Sorting algorithm          Best Case          Average Case         Worst Case          space          stable
Selection Sort	              O(n2)	               O(n2)	           O(n2)            O(1)            No
'''


# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''