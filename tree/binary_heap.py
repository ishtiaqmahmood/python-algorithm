class Heap:
    """
    A class to represent a Binary Heap.
    """
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1


def peek_of_heap(root_node):
    """
    Returns the root element of the heap.
    """
    if not root_node or root_node.heap_size == 0:
        return None
    return root_node.custom_list[1]


def size_of_heap(root_node):
    """
    Returns the current size of the heap.
    """
    if not root_node:
        return 0
    return root_node.heap_size


def level_order_traversal(root_node):
    """
    Performs level-order traversal of the heap.
    """
    if not root_node:
        return
    for i in range(1, root_node.heap_size + 1):
        print(root_node.custom_list[i])


def heapify_tree_insert(root_node, index, heap_type):
    """
    Maintains the heap property after an insertion.
    """
    parent_index = int(index / 2)
    if index <= 1:
        return
    if heap_type == "Min":
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            root_node.custom_list[index], root_node.custom_list[parent_index] = \
                root_node.custom_list[parent_index], root_node.custom_list[index]
            heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == "Max":
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            root_node.custom_list[index], root_node.custom_list[parent_index] = \
                root_node.custom_list[parent_index], root_node.custom_list[index]
            heapify_tree_insert(root_node, parent_index, heap_type)


def insert_node(root_node, node_value, heap_type):
    """
    Inserts a new node into the heap.
    """
    if root_node.heap_size + 1 == root_node.max_size:
        return "The Binary Heap is Full"
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)
    return "The value has been successfully inserted"


def heapify_tree_extract(root_node, index, heap_type):
    """
    Maintains the heap property after an extraction.
    """
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0

    if root_node.heap_size < left_index:
        return
    elif root_node.heap_size == left_index:
        if heap_type == "Min":
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                root_node.custom_list[index], root_node.custom_list[left_index] = \
                    root_node.custom_list[left_index], root_node.custom_list[index]
        else:
            if root_node.custom_list[index] < root_node.custom_list[left_index]:
                root_node.custom_list[index], root_node.custom_list[left_index] = \
                    root_node.custom_list[left_index], root_node.custom_list[index]
        return
    else:
        if heap_type == "Min":
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] > root_node.custom_list[swap_child]:
                root_node.custom_list[index], root_node.custom_list[swap_child] = \
                    root_node.custom_list[swap_child], root_node.custom_list[index]
                heapify_tree_extract(root_node, swap_child, heap_type)
        else:
            if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] < root_node.custom_list[swap_child]:
                root_node.custom_list[index], root_node.custom_list[swap_child] = \
                    root_node.custom_list[swap_child], root_node.custom_list[index]
                heapify_tree_extract(root_node, swap_child, heap_type)


def extract_node(root_node, heap_type):
    """
    Removes and returns the root element of the heap.
    """
    if root_node.heap_size == 0:
        return None
    extracted_node = root_node.custom_list[1]
    root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
    root_node.custom_list[root_node.heap_size] = None
    root_node.heap_size -= 1
    heapify_tree_extract(root_node, 1, heap_type)
    return extracted_node


def delete_entire_bh(root_node):
    """
    Deletes the entire heap.
    """
    root_node.custom_list = None


if __name__ == "__main__":
    new_binary_heap = Heap(5)
    insert_node(new_binary_heap, 4, "Max")
    insert_node(new_binary_heap, 1, "Max")
    insert_node(new_binary_heap, 5, "Max")
    insert_node(new_binary_heap, 3, "Max")
    print("Level order traversal after insertions:")
    level_order_traversal(new_binary_heap)

    print(f"Extracted: {extract_node(new_binary_heap, 'Max')}")
    print("Level order traversal after extraction:")
    level_order_traversal(new_binary_heap)
