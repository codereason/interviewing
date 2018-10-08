'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # def inorderTraversal_(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if root == None:
    #         return []
    #     # print(root.val+" ")
    #     list = [root.val]
    #
    #     left = self.inorderTraversal(root.left)
    #     right = self.inorderTraversal(root.right)
    #     print (list + left + right)
    #     return  left +list   + right

    def inorderTraversal(self, root):
        stack = []
        list = []
        if root == None:
            return []
        else:

            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                    # 把树的左边界都往栈压

                else:
                    root = stack.pop()
                    list.append(root.val)
                    root = root.right

            return list
