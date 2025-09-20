from typing import Optional
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        
        invertTree(root.left)
        invertTree(root.right)

        return root
def print_tree(node: Optional[TreeNode], level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        print_tree(node.left, level + 1)

# Example usage:
if __name__ == "__main__":
    # Construct a binary tree
    #       1
    #     /  \
    #    2     3
    #   / \    / \
    #  4   5  6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print_tree(root)
    print_tree(invertTree(root))