class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    Serialization and Deserialization of Binary Tree.
    """
    def serialize(self, root):
        if not root: return "None,"
        return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        def helper(nodes):
            val = nodes.pop(0)
            if val == "None": return None
            node = TreeNode(int(val))
            node.left = helper(nodes)
            node.right = helper(nodes)
            return node

        return helper(data.split(',')[:-1])


if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3); root.right.left = TreeNode(4)
    serialized = codec.serialize(root)
    print(f"Serialized: {serialized}")
    deserialized = codec.deserialize(serialized)
    print(f"Deserialized root val: {deserialized.val}")
