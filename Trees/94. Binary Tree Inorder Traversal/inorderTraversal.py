from typing import Optional
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: Optional[TreeNode]) -> list[int]:
    result = []
    def traverse(node: Optional[TreeNode]):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    traverse(root)
    return result

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

    # Perform inorder traversal
    print(inorderTraversal(root))  # Output: [4, 2, 5, 1, 6, 3, 7]