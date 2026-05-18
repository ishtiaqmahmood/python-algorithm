def gnome_sort(arr):
    """
    Gnome Sort.
    """
    index = 0
    while index < len(arr):
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr


if __name__ == "__main__":
    print(f"Gnome Sort: {gnome_sort([34, 2, 10, -9])}")
