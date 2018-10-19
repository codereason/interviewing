'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.is_Revert(root.left, root.right)

    def is_Revert(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 and root2:
            if root1.val == root2.val and self.is_Revert(root1.left,
                                                         root2.right) and self.is_Revert(
                root1.right, root2.left):
                return True
            else:
                return False
        else:
            return False
