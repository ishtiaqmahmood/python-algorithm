from collections import deque

class TreeNode:
    """
    A class to represent a node in a Binary Tree.
    """
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def pre_order_traversal(root_node):
    """
    Performs pre-order traversal of the Binary Tree.
    """
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):
    """
    Performs in-order traversal of the Binary Tree.
    """
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    """
    Performs post-order traversal of the Binary Tree.
    """
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):
    """
    Performs level-order traversal of the Binary Tree using a deque.
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


def search_bt(root_node, node_value):
    """
    Searches for a node with node_value in the Binary Tree.
    """
    if not root_node:
        return "The BT does not exist"
    queue = deque([root_node])
    while queue:
        root = queue.popleft()
        if root.data == node_value:
            return "Success"
        if root.left_child is not None:
            queue.append(root.left_child)
        if root.right_child is not None:
            queue.append(root.right_child)
    return "Not found"


def insert_node_bt(root_node, new_node):
    """
    Inserts a node into the Binary Tree at the first available position.
    """
    if not root_node:
        return new_node
    queue = deque([root_node])
    while queue:
        root = queue.popleft()
        if root.left_child is not None:
            queue.append(root.left_child)
        else:
            root.left_child = new_node
            return "Successfully Inserted"
        if root.right_child is not None:
            queue.append(root.right_child)
        else:
            root.right_child = new_node
            return "Successfully Inserted"


def get_deepest_node(root_node):
    """
    Returns the deepest node in the Binary Tree.
    """
    if not root_node:
        return None
    queue = deque([root_node])
    root = None
    while queue:
        root = queue.popleft()
        if root.left_child is not None:
            queue.append(root.left_child)
        if root.right_child is not None:
            queue.append(root.right_child)
    return root


def delete_deepest_node(root_node, d_node):
    """
    Deletes the given deepest node from the Binary Tree.
    """
    if not root_node:
        return
    queue = deque([root_node])
    while queue:
        root = queue.popleft()
        if root is d_node:
            root = None
            return
        if root.right_child:
            if root.right_child is d_node:
                root.right_child = None
                return
            else:
                queue.append(root.right_child)
        if root.left_child:
            if root.left_child is d_node:
                root.left_child = None
                return
            else:
                queue.append(root.left_child)


def delete_node_bt(root_node, node_data):
    """
    Deletes a node with node_data from the Binary Tree.
    """
    if not root_node:
        return "The BT does not exist"
    queue = deque([root_node])
    while queue:
        root = queue.popleft()
        if root.data == node_data:
            d_node = get_deepest_node(root_node)
            root.data = d_node.data
            delete_deepest_node(root_node, d_node)
            return "The node has been successfully deleted"
        if root.left_child is not None:
            queue.append(root.left_child)
        if root.right_child is not None:
            queue.append(root.right_child)
    return "Failed to delete"


def delete_bt(root_node):
    """
    Deletes the entire Binary Tree.
    """
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The BT has been successfully deleted"


if __name__ == "__main__":
    new_bt = TreeNode("Drinks")
    left_child = TreeNode("Hot")
    right_child = TreeNode("Cold")
    new_bt.left_child = left_child
    new_bt.right_child = right_child

    insert_node_bt(new_bt, TreeNode("Tea"))
    insert_node_bt(new_bt, TreeNode("Coffee"))

    print("Level Order Traversal:")
    level_order_traversal(new_bt)

    delete_node_bt(new_bt, "Hot")
    print("Level Order Traversal after deleting 'Hot':")
    level_order_traversal(new_bt)
