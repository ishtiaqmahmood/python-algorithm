class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """
    Implementation of an AVL Tree (Self-Balancing BST).
    """
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        # Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root: return 0
        return root.height

    def get_balance(self, root):
        if not root: return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if not root: return
        print(f"{root.val} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

if __name__ == "__main__":
    avl = AVLTree()
    root = None
    nums = [10, 20, 30, 40, 50, 25]
    for n in nums:
        root = avl.insert(root, n)
    print("Pre-order traversal of AVL tree:")
    avl.pre_order(root)
    print()
