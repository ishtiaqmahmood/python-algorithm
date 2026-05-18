import random


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]: return False
    return True


def bogo_sort(arr):
    """
    Bogo Sort (Random permutation sort).
    """
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr


if __name__ == "__main__":
    print(f"Bogo Sort: {bogo_sort([3, 1, 2])}")
