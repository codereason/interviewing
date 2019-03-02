# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, rootA, rootB):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if rootA is None: return False
        return self.is_same_tree(rootA, rootB) or self.isSubtree(rootA.right, rootB) or self.isSubtree(rootA.left,
                                                                                                       rootB)

    def is_same_tree(self, rootA, rootB):

        if rootA and rootB:
            return rootA.val == rootB.val and self.is_same_tree(rootA.left, rootB.left) and self.is_same_tree(
                rootA.right, rootB.right)
        elif rootA is None and rootB is None:
            return True
        else:
            return False
