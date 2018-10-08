'''

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []
        # print(root.val+" ")
        list = [root.val]

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return list + left + right

    def preorderTraversal2(self, root):
        stack = []
        list = []
        if root == None:
            return []
        else:

            stack.append(root)
            while (stack):
                root = stack.pop()
                list.append(root.val)
                print(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
            return list
