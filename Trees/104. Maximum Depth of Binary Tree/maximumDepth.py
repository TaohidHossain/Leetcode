from typing import Optional
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# Example usage:
if __name__ == "__main__":
    # Construct a binary tree
    #       1
    #     /  \
    #    2    3
    #   / \   / \
    #  4   5 6   7
    #             \
    #              8
    #               \
    #                9
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    root.right.right.right.right = TreeNode(9)

    print(maxDepth(root))  # Output: 5