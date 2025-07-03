"""
Given an array arr. The task is to find the largest element in the given array. 

Examples: 

Input: arr[] = [10, 20, 4]
Output: 20
Explanation: Among 10, 20 and 4, 20 is the largest. 

Input: arr[] = [20, 10, 20, 4, 100]
Output: 100

"""

def findLargest(arr):
    maxEl=arr[0]

    for i in range(1,len(arr)):
        if arr[i]>maxEl:
             maxEl=arr[i] 
    return maxEl

# print(findLargest([20, 10, 20, 4, 100]))
# Time: O(n)
# Space: O(1)

def findMax(arr, i):
  
    # Last index returns the element
    if i == len(arr) - 1:
        return arr[i]

    # Find the maximum from the rest of the list
    recMax = findMax(arr, i + 1)

    # Compare with i-th element and return
    return max(recMax, arr[i])


def largest(arr):
    return findMax(arr, 0)

arr = [10, 324, 45, 90, 9808]
print(largest(arr))