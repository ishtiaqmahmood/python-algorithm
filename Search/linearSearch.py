def linearSearch(arr, n, x):
    for i in range(0,n):
        if (arr[i] == x):
            return i
    return -1

# Driver code
arr = [2,5,4,7,6,3,9,8,1]
x = 66
n = len(arr)

# Function call
result = linearSearch(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present in index ", result)
