# Iterative Ternary Search
def ternarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    while high >= low:

        # Find mid1 and mid2
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        # Check if key is at any mid
        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2

        # Since key is not present at mid,
        # Check in which region it is present
        # Then repeat the search operation in that region
        if key < arr[mid1]:
            # key lies between l and mid1
            high = mid1 - 1
        elif key > arr[mid2]:
            # key lies between mid2 and r
            low = mid2 + 1
        else:
            # key lies between mid1 and mid2
            low = mid1 + 1
            high = mid2 - 1

    # key not found
    return -1


# Driver code

# Get the list
# Sort the list if not sorted
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Checking for 5
# Key to be searched in the list
key = 5

# Search the key using ternary search
result = ternarySearch(arr, key)

# Print the result
if (result != -1):
    print("Element found at index ", result)
else:
    print("Element is not found in array")