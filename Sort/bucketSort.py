import math


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList
    

def bucketSort(customList):
    numofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*numofBuckets/maxValue)
        arr[index_b-1].append(j)
    for i in range(numofBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    print(customList)


list = [2,9,6,3,1,4,7,5,8]
bucketSort(list)

