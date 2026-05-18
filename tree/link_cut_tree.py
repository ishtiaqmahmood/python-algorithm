class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = self.parent = None


def is_root(x):
    return not x.parent or (x.parent.left != x and x.parent.right != x)


def rotate(x):
    y = x.parent
    z = y.parent
    if not is_root(y):
        if z.left == y: z.left = x
        else: z.right = x
    x.parent = z
    if y.left == x:
        y.left = x.right
        if x.right: x.right.parent = y
        x.right = y
    else:
        y.right = x.left
        if x.left: x.left.parent = y
        x.left = y
    y.parent = x


def splay(x):
    while not is_root(x):
        y = x.parent
        z = y.parent
        if not is_root(y):
            if (z.left == y) == (y.left == x): rotate(y)
            else: rotate(x)
        rotate(x)


def access(x):
    last = None
    curr = x
    while curr:
        splay(curr)
        curr.right = last
        last = curr
        curr = curr.parent
    splay(x)


if __name__ == "__main__":
    print("Link-Cut Tree basic operations defined.")
