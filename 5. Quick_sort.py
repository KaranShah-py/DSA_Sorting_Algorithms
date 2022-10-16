# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''

'''
Quick Sort
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. 
It picks an element as pivot and partitions the given array around the picked pivot. 
There are many different versions of quickSort that pick pivot in different ways. 

Some of the ways are :
    Always pick first element as pivot.
    Always pick last element as pivot (implemented below)
    Pick a random element as pivot.
    Pick median as pivot.
The key process in quickSort is partition(). 
Target of partitions is, given an array and an element x of array as pivot, 
put x at its correct position in sorted array and put all 
smaller elements (smaller than x) before x, 
and put all greater elements (greater than x) after x. 
All this should be done in linear time.

Time complexity : 
The time complexity for the quick sort is :
Best Case                    Average Case                   Worst Case
O(nlogn)                       O(nlogn)                       o(n^2)
'''
# functions 
def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    
    while start < end:
         
        while start < len(array) and array[start] <= pivot:
            start += 1
             
        while array[end] > pivot:
            end -= 1

        if(start < end):
            array[start], array[end] = array[end], array[start]
        
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end
     
# The main function that implements QuickSort
def quick_sort(start, end, array):
    if start < end:
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)




'''
Sorting algorithm          Best Case          Average Case         Worst Case          space          stable
Quick Sort	                  O(n.log(n))	       O(n.log(n))	       O(n2)            O(nlogn)        No
'''

# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''