# Recursive Binary Search

def recursive_binary_search(arr, low, high, key):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == key:
            return mid

        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > key:
            return recursive_binary_search(arr, low, mid - 1, key)

        # Else the element can only be present in right subarray
        else:
            return recursive_binary_search(arr, mid + 1, high, key)

    else:
        # Element is not present in the array
        return -1


# Iterative Binary Search
def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Check if key present at mid
        if arr[mid] < key:
            low = mid + 1

        # If key is greater, ignore left half
        elif arr[mid] > key:
            high = mid - 1

        # If key is smaller, ignore right half

        else:
            return mid

    # If we reach here, then the element was not present
    return -1

list = [1,2,3,4,5,6,7,8,9]
key = 6

# Function call
#result = recursive_binary_search(arr, 0, len(arr)-1, key)
result = binarySearch(list, key)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")