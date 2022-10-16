# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''

'''
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
The array is virtually split into a sorted and an unsorted part. 
Values from the unsorted part are picked and placed at the correct position in the sorted part.
Algorithm 
To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, 
   compare it to the elements before. Move the greater elements 
   one position up to make space for the swapped element.
Example: 
insertion-sort
12, 11, 13, 5, 6
Let us loop for i = 1 (second element of the array) to 4 (last element of the array)

i = 1. 
Comparing 1 with its predecessor that is i = 0.
Since 11 is smaller than 12, move 12 and insert 11 before 12 
11, 12, 13, 5, 6

i = 2. 
S13 will remain at its position as all elements in A[0..I-1] are smaller than 13 
11, 12, 13, 5, 6

i = 3. 
5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position. 
5, 11, 12, 13, 6

i = 4. 
6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position. 
5, 6, 11, 12, 13
'''
# functions 
def insertion_sort_asc(arr, n):
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > temp:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            else:
                break

def insertion_sort_desc(arr, n):
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] < temp:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            else:
                break

# Driver code
arr = [5,6,4,3,8,2,1]
print(arr)
insertion_sort_asc(arr, len(arr))
print(arr)
insertion_sort_desc(arr, len(arr))
print(arr)

'''
Sorting algorithm          Best Case          Average Case         Worst Case          space          stable
Insertion Sort	              O(n)	               O(n2)	           O(n2)            O(1)            Yes
'''

# Code by Karan Shah 
'''
Linkedin: - https://www.linkedin.com/in/karan-shah2001/
GitHub: - https://github.com/KaranShah-py
Leetcode: - https://leetcode.com/karanshah007/
'''