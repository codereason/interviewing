'''
404. Sum of Left Leaves
Easy

779

92

Favorite

Share
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def is_children(self, root):
        if root.left is None and root.right is None:
            return True

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right:
            return root.left.val

        if root.left is None and root.right:
            return self.sumOfLeftLeaves(root.right)

        if root.right is None and root.left:
            return self.sumOfLeftLeaves(root.left)

        if root.left and root.right:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)