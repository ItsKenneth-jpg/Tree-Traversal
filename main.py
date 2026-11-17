class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def get_preorder(root, result=None):
    """Root -> Left -> Right"""
    if result is None:
        result = []
    if root:
        result.append(root.val)
        get_preorder(root.left, result)
        get_preorder(root.right, result)
    return result


def get_inorder(root, result=None):
    """Left -> Root -> Right"""
    if result is None:
        result = []
    if root:
        get_inorder(root.left, result)
        result.append(root.val)
        get_inorder(root.right, result)
    return result


def get_postorder(root, result=None):
    """Left -> Right -> Root"""
    if result is None:
        result = []
    if root:
        get_postorder(root.left, result)
        get_postorder(root.right, result)
        result.append(root.val)
    return result


if __name__ == "__main__":

    root = Node('K')

    # Level 1
    root.left = Node('E')
    root.right = Node('N')

    # Level 2
    root.left.left = Node('N')
    root.left.right = Node('E')
    root.right.left = Node('T')
    root.right.right = Node('H')

    # Level 3
    root.left.left.left = Node('C')
    root.left.left.right = Node('A')
    root.left.right.left = Node('N')
    root.left.right.right = Node('O')
    root.right.left.left = Node('N')

    # Output DFS Traversals
    print("--- KENNETH CANON Binary Tree Traversals ---")
    print("PreOrder :", " -> ".join(get_preorder(root)))
    print("InOrder  :", " -> ".join(get_inorder(root)))
    print("PostOrder:", " -> ".join(get_postorder(root)))