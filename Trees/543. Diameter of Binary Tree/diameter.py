from typing import Optional
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    max_diameter = 0

    def depth(node: Optional[TreeNode]) -> int:
        nonlocal max_diameter
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        max_diameter = max(max_diameter, left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    depth(root)
    return max_diameter


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

    print(diameterOfBinaryTree(root))  # Output: 6