""""
Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12

"""


def printAlternates(arr):
    res=[]

    for i in range(0,len(arr),2):
        res.append(arr[i])

    return res

# print(printAlternates([-5, 1, 4, 2, 12]))
# Time Complexity: O(n), where n is the number of elements in arr[].
# Auxiliary Space: O(1)

def getAlternatives(arr): 

    res=[]

    for i in range(len(arr)):
        if i % 2 == 0:
            res.append(arr[i])

    return res

# print(getAlternatives([-5, 1, 4, 2, 12]))
# Time Complexity: O(n), where n is the number of elements in arr[].
# Auxiliary Space: O(1)

def getAlternatesRec(arr,idx,res):
    if idx<len(arr):
        res.append(arr[idx]);
        getAlternatesRec(arr,idx+2,res)
def getAlternatesRecApp(arr):
    res=[]

    getAlternatesRec(arr,0,res)
    return res
print(getAlternatesRecApp([10, 20, 30, 40, 50])) # [10,30,50]. => res.join(" ")

# Time Complexity: O(n), where n is the number of elements in arr[].
# Auxiliary Space: O(n), for recursive call stack.