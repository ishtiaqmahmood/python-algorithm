from collections import deque

class BSTNode:
    """
    A class to represent a node in a Binary Search Tree.
    """
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(root_node, node_value):
    """
    Inserts a node with node_value into the BST.
    """
    if root_node.data is None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BSTNode(node_value)
        else:
            insert_node(root_node.left_child, node_value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BSTNode(node_value)
        else:
            insert_node(root_node.right_child, node_value)
    return "The node has been successfully inserted"


def pre_order_traversal(root_node):
    """
    Performs pre-order traversal of the BST.
    """
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):
    """
    Performs in-order traversal of the BST.
    """
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    """
    Performs post-order traversal of the BST.
    """
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):
    """
    Performs level-order traversal of the BST using a deque.
    """
    if not root_node:
        return
    queue = deque([root_node])
    while queue:
        root = queue.popleft()
        print(root.data)
        if root.left_child is not None:
            queue.append(root.left_child)
        if root.right_child is not None:
            queue.append(root.right_child)


def search_node(root_node, node_value):
    """
    Searches for a node with node_value in the BST.
    """
    if root_node is None:
        return "Not found"
    if root_node.data == node_value:
        return "The value is found"
    elif node_value < root_node.data:
        return search_node(root_node.left_child, node_value)
    else:
        return search_node(root_node.right_child, node_value)


def min_value_node(bst_node):
    """
    Finds the node with the minimum value in the BST.
    """
    current = bst_node
    while current.left_child is not None:
        current = current.left_child
    return current


def delete_node(root_node, node_value):
    """
    Deletes a node with node_value from the BST.
    """
    if root_node is None:
        return root_node
    if node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp

        temp = min_value_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    return root_node


def delete_bst(root_node):
    """
    Deletes the entire BST.
    """
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The BST has been successfully deleted"


if __name__ == "__main__":
    new_bst = BSTNode(None)
    insert_node(new_bst, 40)
    insert_node(new_bst, 70)
    insert_node(new_bst, 30)
    insert_node(new_bst, 50)
    insert_node(new_bst, 60)
    insert_node(new_bst, 80)
    insert_node(new_bst, 20)

    print("Level Order Traversal:")
    level_order_traversal(new_bst)

    print(f"Search 60: {search_node(new_bst, 60)}")
    delete_node(new_bst, 50)
    print("Level Order Traversal after deleting 50:")
    level_order_traversal(new_bst)
