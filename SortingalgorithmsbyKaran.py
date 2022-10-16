# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''

'''
Save this file in your local system and next time if you want to use 
any of the sorting algorithms from [selectionsort, bubblesort, insertionsort, quicksort, mergesort]
then just import everthing from SortingalgorithmsbyKaran
and use the function.

from SortingalgorithmsbyKaran import *
list1 = [10,20,3,2,100]
SortingalgorithmsbyKaran.bubblesort(list1)
'''

# selection sort 
class SortingalgorithmsbyKaran:
    def __init__(self) -> None:
        pass

    @staticmethod
    def selectionsort(arr:list, sortas='ASC'):
        '''
        arguments: - List, sortas - ['ASC' OR 'DESC']
        '''
        sortas = sortas.upper()
        if sortas not in ['ASC', 'DESC']:
            raise Exception("Please enter ASC or DESC")
        else:
            # sort the elements in ascending order
            if sortas == "ASC":
                for i in range(0, len(arr)-1):
                    minimum_element_index = i
                    for j in range(i+1, len(arr)):
                        if arr[minimum_element_index] > arr[j]:
                            minimum_element_index = j
                    arr[i], arr[minimum_element_index] = arr[minimum_element_index], arr[i]

            # sort the elements in descending order
            else:
                if sortas == "ASC":
                    for i in range(0, len(arr)-1):
                        maximum_element_index = i
                        for j in range(i+1, len(arr)):
                            if arr[maximum_element_index] < arr[j]:
                                maximum_element_index = j
                        arr[i], arr[maximum_element_index] = arr[maximum_element_index], arr[i]

    # Bubble sort function
    @staticmethod
    def bubblesort(arr:list, sortas='ASC'):
        sortas = sortas.upper()
        if sortas not in ['ASC', 'DESC']:
            raise Exception("Please enter ASC or DESC")
        else:
            # code sort the elements in ascending order
            if sortas == "ASC":
                for i in range(0, len(arr) - 1):
                    swaps = 0
                    for j in range(0, len(arr)-1-i):
                        if arr[j] > arr[j+1]:
                            arr[j], arr[j+1] = arr[j+1], arr[j]
                            swaps = 1
                    if swaps == 0:
                        break
            # code sort the elements in descending order
            else:
                for i in range(0, len(arr) - 1):
                    swaps = 0
                    for j in range(0, len(arr)-1-i):
                        if arr[j] < arr[j+1]:
                            arr[j], arr[j+1] = arr[j+1], arr[j]
                            swaps = 1
                    if swaps == 0:
                        break
        

    @staticmethod
    def insertionsort(arr, sortas = 'ASC'):
        '''
        arguments: - List, sortas - ['ASC' OR 'DESC']
        '''
        sortas = sortas.upper()
        if sortas not in ['ASC', 'DESC']:
            raise Exception("Please enter ASC or DESC")
        else:
            # code sort the elements in ascending order
            if sortas == "ASC":
                for i in range(1, len(arr)):
                    temp = arr[i]
                    for j in range(i-1, -1, -1):
                        if arr[j] > temp:
                            arr[j], arr[j+1] =  arr[j+1], arr[j]
                        else:
                            break
            # code sort the elements in descending order
            else:
                for i in range(1, len(arr)):
                    temp = arr[i]
                    for j in range(i-1, -1, -1):
                        if arr[j] < temp:
                            arr[j], arr[j+1] =  arr[j+1], arr[j]
                        else:
                            break
    
    # Merge sort code for sorting in ascending order.
    def __mergeforasc(arr, lower, upper):
        i = j = k = 0
        
        while i < len(lower) and j < len(upper):
            if lower[i] < upper[j]:
                arr[k] = lower[i]
                i += 1
            else:
                arr[k] = upper[j]
                j += 1
            k += 1
        
        while i < len(lower):
            arr[k] = lower[i]
            i += 1
            k += 1

        while j < len(upper):
            arr[k] = upper[j]
            j += 1
            k += 1

    # Merge sort code for sorting in descending order.
    def __mergefordesc(arr, lower, upper):
        i = j = k = 0
        
        while i < len(lower) and j < len(upper):
            if lower[i] > upper[j]:
                arr[k] = lower[i]
                i += 1
            else:
                arr[k] = upper[j]
                j += 1
            k += 1
        
        while i < len(lower):
            arr[k] = lower[i]
            i += 1
            k += 1

        while j < len(upper):
            arr[k] = upper[j]
            j += 1
            k += 1


    @staticmethod
    def mergesort(arr:list, sortas = "ASC"):
        '''
        arguments: - List, sortas - ['ASC' OR 'DESC']
        '''
        sortas = sortas.upper()
        if sortas not in ['ASC', 'DESC']:
            raise Exception("Please enter ASC or DESC")
        else:
            if len(arr) > 1:
                mid = len(arr) // 2
                lower_array = arr[0:mid]
                upper_array = arr[mid:]
                SortingalgorithmsbyKaran.mergesort(lower_array)
                SortingalgorithmsbyKaran.mergesort(upper_array)
                if sortas == 'ASC':
                    SortingalgorithmsbyKaran.__mergeforasc(arr, lower_array, upper_array)
                else:
                    SortingalgorithmsbyKaran.__mergefordesc(arr, lower_array, upper_array)  

    
    # Quick sort code for sorting in ascending order.
    def __quicksortpartitionforasc(start:int, end:int,array:list) -> int:
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

    # Merge sort code for sorting in descending order.
    def __quicksortpartitionfordesc(start:int, end:int,array:list) -> int:
        pivot_element_index = start
        pivot_element = array[start]

        while start < end:
            while start < len(array) and array[start] >= pivot_element:
                start += 1

            while array[end] < pivot_element:
                end -= 1

            if start < end:
                array[start], array[end] = array[end], array[start]
        
        array[pivot_element_index], array[end] = array[end], array[pivot_element_index]
        return end

    @staticmethod
    def quicksort(start,end,array, sortas='ASC'):
        '''
        arguments: - 
        start_index, end_index,
        List, sortas - ['ASC' OR 'DESC']
        '''
        sortas = sortas.upper()
        if sortas not in ['ASC', 'DESC']:
            raise Exception("Please enter ASC or DESC")
        else:
            if start < end:
                if sortas == 'ASC':
                    p = SortingalgorithmsbyKaran.__quicksortpartitionforasc(start, end, array)
                else:
                    p = SortingalgorithmsbyKaran.__quicksortpartitionfordesc(start, end, array)
                SortingalgorithmsbyKaran.quicksort(start, p-1, array, sortas)
                SortingalgorithmsbyKaran.quicksort(p+1, end, array, sortas)


# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''