'''
iven a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.


'''
# Definition for a binary tree node.
'''
会TLE
但是可以用

'''
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:return True
        if self.isBalanced(root.left) and self.isBalanced(root.right) and \
            abs(self._getSubTreeLength(root.left) - self._getSubTreeLength(root.right)) <= 1:
            return True
        # print(abs(self._getSubTreeLength(root.left) - self._getSubTreeLength(root.right)))
        return False

    def _getSubTreeLength(self,root):
        if root is None: return 0
        return 1 + max(self._getSubTreeLength(root.left),self._getSubTreeLength(root.right))



class Solution2:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:return True

        if abs(self._getSubTreeLength(root.left) - self._getSubTreeLength(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        # print(abs(self._getSubTreeLength(root.left) - self._getSubTreeLength(root.right)))
        else:return False

    def _getSubTreeLength(self,root):
        if root is None: return 0
        return 1+ max(self._getSubTreeLength(root.left),self._getSubTreeLength(root.right))

